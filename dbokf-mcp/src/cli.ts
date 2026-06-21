#!/usr/bin/env node
import { Command } from 'commander';
import path from 'path';
import { startServer } from './server.js';
import { buildIndex } from './indexer.js';

const program = new Command();

program
  .name('dbokf-mcp')
  .description('MCP server for the Databricks OKF knowledge base')
  .version('1.0.0')
  .addHelpCommand(false);

program
  .command('server')
  .description('Start the MCP server (stdio transport)')
  .option('--okf-dir <path>', 'Path to OKF root directory', process.cwd())
  .action(async (opts: { okfDir: string }) => {
    try {
      await startServer(path.resolve(opts.okfDir));
    } catch (err) {
      console.error('Error:', err instanceof Error ? err.message : String(err));
      process.exit(1);
    }
  });

program
  .command('index')
  .description('Build the embedding index — required before first use')
  .option('--okf-dir <path>', 'Path to OKF root directory', process.cwd())
  .option('--batch-size <n>', 'API batch size (default: 100)', '100')
  .action(async (opts: { okfDir: string; batchSize: string }) => {
    try {
      await buildIndex(path.resolve(opts.okfDir), parseInt(opts.batchSize, 10));
    } catch (err) {
      console.error('Error:', err instanceof Error ? err.message : String(err));
      process.exit(1);
    }
  });

program
  .command('help')
  .description('Show detailed usage and configuration guide')
  .action(() => {
    console.log(`
dbokf-mcp — Databricks OKF MCP Server
======================================

COMMANDS
  index    Build the embedding index (run once before first use)
  server   Start the MCP server on stdio
  help     Show this guide

SETUP
  1. Install globally:
       npm install -g dbokf-mcp

  2. Set your API key and optionally a custom endpoint and model:
       export LLM_KEY=sk-...
       export LLM_BASE_URL=https://openrouter.ai/api/v1         # optional, defaults to OpenAI
       export LLM_EMBEDDING_MODEL=perplexity/pplx-embed-v1-0.6b # optional, default: text-embedding-3-small

  3. Build the index (one-time, ~5 min for 6000+ concepts):
       dbokf-mcp index --okf-dir /path/to/okf

  4. Start the server:
       dbokf-mcp server --okf-dir /path/to/okf

CONFIGURE WITH CLAUDE
  Add to claude_desktop_config.json or .claude/settings.json:

  With OpenAI (default):
    {
      "mcpServers": {
        "databricks-okf": {
          "command": "dbokf-mcp",
          "args": ["server", "--okf-dir", "/path/to/okf"],
          "env": { "LLM_KEY": "sk-..." }
        }
      }
    }

  With OpenRouter:
    {
      "mcpServers": {
        "databricks-okf": {
          "command": "dbokf-mcp",
          "args": ["server", "--okf-dir", "/path/to/okf"],
          "env": {
            "LLM_KEY": "sk-or-...",
            "LLM_BASE_URL": "https://openrouter.ai/api/v1",
            "LLM_EMBEDDING_MODEL": "perplexity/pplx-embed-v1-0.6b"
          }
        }
      }
    }

ENVIRONMENT VARIABLES
  LLM_KEY               API key (required)
  LLM_BASE_URL          API endpoint (optional, defaults to OpenAI)
  LLM_EMBEDDING_MODEL   Embedding model (optional, default: text-embedding-3-small)
                        The model used at index time is stored in dbokf-index/config.json
                        and reused automatically by 'server'. Override with this var.

MCP TOOLS (exposed to LLM clients)
  search_concepts(query, k=5)       Semantic search over all concepts
  fetch_concept(id)                  Get full concept markdown by ID
  search_by_tags(tags, limit=10)    Filter concepts by tag (all must match)
  list_tags()                        List all available tags

INDEX FILES (created by 'index' command)
  <okf-dir>/dbokf-index/meta.json     Concept metadata (id, title, tags)
  <okf-dir>/dbokf-index/vectors.bin   Binary Float32 embeddings (~37 MB)

EMBEDDING MODEL
  text-embedding-3-small (OpenAI) — 1536 dimensions
  Approx. cost for 6000+ concepts: ~$0.10
`);
  });

program.parse();
