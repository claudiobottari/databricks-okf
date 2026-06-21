import { readFileSync } from 'fs';
import matter from 'gray-matter';

export interface ConceptMeta {
  id: string;
  title: string;
  description: string;
  tags: string[];
}

export interface Concept extends ConceptMeta {
  content: string;
  filePath: string;
}

export function parseConcept(filePath: string, id: string): Concept {
  const raw = readFileSync(filePath, 'utf-8');
  const { data } = matter(raw);

  return {
    id,
    title: typeof data.title === 'string' ? data.title : id,
    description: typeof data.description === 'string' ? data.description : '',
    tags: Array.isArray(data.tags) ? data.tags.map(String) : [],
    content: raw,
    filePath,
  };
}

export function embedText(c: ConceptMeta): string {
  return [c.title, c.description, c.tags.join(' ')].join('\n').trim();
}

export function cleanContent(raw: string): string {
  const { content } = matter(raw);
  return content.trim();
}
