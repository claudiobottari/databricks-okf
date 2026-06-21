import { readdirSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import path from 'path';
import OpenAI from 'openai';
import { parseConcept, embedText, type ConceptMeta } from './parser.js';

const DEFAULT_MODEL = 'text-embedding-3-small';

export async function buildIndex(okfDir: string, batchSize: number): Promise<void> {
  const key = process.env.LLM_KEY;
  if (!key) throw new Error('LLM_KEY environment variable is required');

  const model = process.env.LLM_EMBEDDING_MODEL ?? DEFAULT_MODEL;
  const baseURL = process.env.LLM_BASE_URL;

  const conceptsDir = path.join(okfDir, 'concepts');
  if (!existsSync(conceptsDir)) {
    throw new Error(`concepts/ directory not found in: ${okfDir}`);
  }

  const files = readdirSync(conceptsDir).filter(f => f.endsWith('.md')).sort();
  console.log(`Found ${files.length} concepts in ${conceptsDir}`);
  console.log(`Model: ${model}${baseURL ? ` via ${baseURL}` : ''} | Batch size: ${batchSize}`);

  const openai = new OpenAI({ apiKey: key, ...(baseURL ? { baseURL } : {}) });

  const metas: ConceptMeta[] = [];
  const allEmbeddings: number[][] = [];
  let dim = 0;

  for (let i = 0; i < files.length; i += batchSize) {
    const batch = files.slice(i, i + batchSize);
    const concepts = batch.map(f =>
      parseConcept(path.join(conceptsDir, f), f.replace(/\.md$/, ''))
    );
    const texts = concepts.map(embedText);

    const pct = Math.round((i / files.length) * 100);
    process.stdout.write(
      `\r[${String(pct).padStart(3)}%] Embedding ${i + 1}–${Math.min(i + batchSize, files.length)} / ${files.length}...`
    );

    const res = await openai.embeddings.create({
      model,
      input: texts,
      encoding_format: 'float',
    });

    for (let j = 0; j < concepts.length; j++) {
      metas.push({
        id: concepts[j].id,
        title: concepts[j].title,
        description: concepts[j].description,
        tags: concepts[j].tags,
      });
      allEmbeddings.push(res.data[j].embedding);
    }

    // Detect dimension from first batch response
    if (dim === 0) dim = allEmbeddings[0].length;
  }

  process.stdout.write('\n');
  console.log(`Embedding dim: ${dim}`);
  console.log('Saving index...');

  const indexDir = path.join(okfDir, 'dbokf-index');
  mkdirSync(indexDir, { recursive: true });

  writeFileSync(path.join(indexDir, 'meta.json'), JSON.stringify(metas));

  // Store model config so server knows which model to use for queries
  writeFileSync(
    path.join(indexDir, 'config.json'),
    JSON.stringify({ model, dim, count: metas.length, indexed_at: new Date().toISOString() }, null, 2)
  );

  const n = allEmbeddings.length;
  const buf = Buffer.allocUnsafe(8 + n * dim * 4);
  buf.writeUInt32LE(n, 0);
  buf.writeUInt32LE(dim, 4);
  const float32 = new Float32Array(buf.buffer, buf.byteOffset + 8, n * dim);
  for (let i = 0; i < n; i++) float32.set(allEmbeddings[i], i * dim);
  writeFileSync(path.join(indexDir, 'vectors.bin'), buf);

  const mb = ((8 + n * dim * 4) / 1024 / 1024).toFixed(1);
  console.log(`Done. ${n} concepts indexed, ${mb} MB written to ${indexDir}`);
}
