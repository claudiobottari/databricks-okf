import { readFileSync, existsSync } from 'fs';
import path from 'path';
import type { ConceptMeta } from './parser.js';

export interface SearchResult {
  meta: ConceptMeta;
  score: number;
}

export class VectorStore {
  private meta: ConceptMeta[] = [];
  private vectors: Float32Array | null = null;
  private norms: Float32Array | null = null;
  private dim = 0;

  load(okfDir: string): void {
    const indexDir = path.join(okfDir, 'dbokf-index');
    const metaPath = path.join(indexDir, 'meta.json');
    const vecPath = path.join(indexDir, 'vectors.bin');

    if (!existsSync(metaPath) || !existsSync(vecPath)) {
      throw new Error(
        `Index not found at ${indexDir}\nRun: dbokf-mcp index --okf-dir "${okfDir}"`
      );
    }

    this.meta = JSON.parse(readFileSync(metaPath, 'utf-8')) as ConceptMeta[];

    const buf = readFileSync(vecPath);
    const ab = buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength) as ArrayBuffer;
    const dv = new DataView(ab);
    const n = dv.getUint32(0, true);
    const d = dv.getUint32(4, true);
    this.dim = d;
    this.vectors = new Float32Array(ab, 8, n * d);

    // Precompute L2 norms for fast cosine similarity
    this.norms = new Float32Array(n);
    for (let i = 0; i < n; i++) {
      let sum = 0;
      const off = i * d;
      for (let j = 0; j < d; j++) sum += this.vectors[off + j] ** 2;
      this.norms[i] = Math.sqrt(sum);
    }
  }

  search(queryEmbedding: number[], k: number): SearchResult[] {
    if (!this.vectors || !this.norms) throw new Error('Store not loaded');

    const q = new Float32Array(queryEmbedding);
    const qNorm = Math.sqrt(q.reduce((s, v) => s + v * v, 0));
    const n = this.meta.length;
    const d = this.dim;

    const scores = new Float32Array(n);
    for (let i = 0; i < n; i++) {
      const off = i * d;
      let dot = 0;
      for (let j = 0; j < d; j++) dot += this.vectors[off + j] * q[j];
      scores[i] = dot / ((this.norms[i] * qNorm) || 1);
    }

    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => scores[b] - scores[a]);

    return idx.slice(0, k).map(i => ({ meta: this.meta[i], score: scores[i] }));
  }

  searchByTags(tags: string[], limit: number): ConceptMeta[] {
    return this.meta.filter(e => tags.every(t => e.tags.includes(t))).slice(0, limit);
  }

  getById(id: string): ConceptMeta | undefined {
    return this.meta.find(e => e.id === id);
  }

  allTags(): string[] {
    const set = new Set<string>();
    for (const e of this.meta) for (const t of e.tags) set.add(t);
    return Array.from(set).sort();
  }

  get size(): number {
    return this.meta.length;
  }
}
