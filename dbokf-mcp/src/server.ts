import { readFileSync, existsSync } from 'fs';
import path from 'path';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  GetPromptRequestSchema,
  ListPromptsRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import OpenAI from 'openai';
import { VectorStore } from './store.js';
import { cleanContent } from './parser.js';

const DEFAULT_MODEL = 'text-embedding-3-small';

interface IndexConfig {
  model: string;
  dim: number;
  count: number;
  indexed_at: string;
}

export async function startServer(okfDir: string): Promise<void> {
  const key = process.env.LLM_KEY;
  if (!key) throw new Error('LLM_KEY environment variable is required');

  const configPath = path.join(okfDir, 'dbokf-index', 'config.json');
  const indexConfig: IndexConfig = existsSync(configPath)
    ? (JSON.parse(readFileSync(configPath, 'utf-8')) as IndexConfig)
    : { model: DEFAULT_MODEL, dim: 1536, count: 0, indexed_at: '' };

  const model = process.env.LLM_EMBEDDING_MODEL ?? indexConfig.model;

  const store = new VectorStore();
  process.stderr.write('[dbokf-mcp] Loading index...\n');
  store.load(okfDir);
  process.stderr.write(
    `[dbokf-mcp] Ready — ${store.size} concepts | model: ${model} | dim: ${indexConfig.dim}\n`
  );

  const baseURL = process.env.LLM_BASE_URL;
  const openai = new OpenAI({ apiKey: key, ...(baseURL ? { baseURL } : {}) });

  const server = new Server(
    { name: 'dbokf-mcp', version: '1.0.0' },
    { capabilities: { tools: {}, prompts: {} } }
  );

  // ── Prompts ──────────────────────────────────────────────────────────────

  server.setRequestHandler(ListPromptsRequestSchema, async () => ({
    prompts: [
      {
        name: 'databricks-assistant',
        description: 'Start a conversation with a Databricks expert backed by the OKF knowledge base',
        arguments: [
          {
            name: 'question',
            description: 'Your Databricks question (optional)',
            required: false,
          },
        ],
      },
    ],
  }));

  server.setRequestHandler(GetPromptRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === 'databricks-assistant') {
      const question = args?.question ?? '';
      return {
        description: 'Databricks expert — OKF knowledge base',
        messages: [
          {
            role: 'user' as const,
            content: {
              type: 'text' as const,
              text: [
                'You are a Databricks expert assistant with access to a structured knowledge base of ' +
                  `${store.size} Databricks concepts via the \`search_databricks\` tool.`,
                '',
                'Rules:',
                '- For ANY question about Databricks, ALWAYS call `search_databricks` first.',
                '- Base your answer strictly on the content returned by the tool.',
                '- If the results are insufficient, call `search_databricks` again with a refined query.',
                '- Use `get_databricks_concept` only when you need deeper detail on a specific concept.',
                '- Never answer Databricks questions from memory alone — always ground in the knowledge base.',
                '',
                question ? `Question: ${question}` : 'Ask me anything about Databricks.',
              ].join('\n'),
            },
          },
        ],
      };
    }

    throw new Error(`Unknown prompt: ${name}`);
  });

  // ── Tools ─────────────────────────────────────────────────────────────────

  server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
      {
        name: 'search_databricks',
        description:
          `Retrieve Databricks documentation from a knowledge base of ${store.size} concepts. ` +
          'Call this for ANY question about Databricks features, APIs, configuration, or best practices. ' +
          'Returns the full text of the most relevant concepts — answer directly from that content.',
        inputSchema: {
          type: 'object',
          properties: {
            query: { type: 'string', description: 'Natural language question or keywords' },
            k: { type: 'number', description: 'Number of concepts to retrieve (default: 3)' },
          },
          required: ['query'],
        },
      },
      {
        name: 'get_databricks_concept',
        description: 'Get the full content of a specific Databricks concept by its ID.',
        inputSchema: {
          type: 'object',
          properties: {
            id: {
              type: 'string',
              description: 'Concept ID (filename without .md, e.g. "delta-lake-checkpointing")',
            },
          },
          required: ['id'],
        },
      },
      {
        name: 'list_databricks_tags',
        description: 'List all topic tags available in the Databricks knowledge base.',
        inputSchema: { type: 'object', properties: {} },
      },
    ],
  }));

  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    process.stderr.write(`[dbokf-mcp] tool: ${name} ${JSON.stringify(args ?? {})}\n`);

    if (name === 'search_databricks') {
      const query = args?.query as string;
      const k = typeof args?.k === 'number' ? args.k : 3;

      const res = await openai.embeddings.create({
        model,
        input: query,
        encoding_format: 'float',
      });

      const results = store.search(res.data[0].embedding, k);

      const parts = results.map(r => {
        const filePath = path.join(okfDir, 'concepts', `${r.meta.id}.md`);
        const body = existsSync(filePath)
          ? cleanContent(readFileSync(filePath, 'utf-8'))
          : r.meta.description;
        return `## ${r.meta.title}\n_tags: ${r.meta.tags.join(', ')}_\n\n${body}`;
      });

      return {
        content: [{ type: 'text', text: parts.join('\n\n---\n\n') }],
      };
    }

    if (name === 'get_databricks_concept') {
      const id = args?.id as string;
      const conceptPath = path.join(okfDir, 'concepts', `${id}.md`);

      if (!existsSync(conceptPath)) {
        return {
          content: [{ type: 'text', text: `Concept '${id}' not found.` }],
          isError: true,
        };
      }

      return {
        content: [{ type: 'text', text: cleanContent(readFileSync(conceptPath, 'utf-8')) }],
      };
    }

    if (name === 'list_databricks_tags') {
      const tags = store.allTags();
      return {
        content: [{ type: 'text', text: JSON.stringify({ count: tags.length, tags }, null, 2) }],
      };
    }

    return {
      content: [{ type: 'text', text: `Unknown tool: ${name}` }],
      isError: true,
    };
  });

  const transport = new StdioServerTransport();
  process.stderr.write('[dbokf-mcp] Listening on stdio (waiting for MCP client)\n');
  await server.connect(transport);
}
