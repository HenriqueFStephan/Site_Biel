import { BlogPost } from '../../core/models';

/** Áreas de atuação (issue #50) — labels must match product copy exactly. */
export const RESEARCH_AREAS = [
  'Medicinal',
  'Agronomia',
  'Construção',
  'Têxtil',
  'Regulatório',
] as const;

export type ResearchArea = (typeof RESEARCH_AREAS)[number];

const CONSTRUCTION_PATTERN =
  /hempcrete|hemp[- ]lime|building engineering|bio-?composite|hemp board|earth[–-]hemp|machining stability in hemp|thermal and acoustic properties|low-carbon binders|hydraulic lime|effect of technological variables on thermal/i;

const CLINICAL_PATTERN =
  /patient|clinical|trial|rct|symptom|pain|cancer|arthritis|driving|edible|pharmacokinetic|postsurgical|sleep|cross-over|dose-dependent|medicinal cannabis|cardiovascular|prenatal|executive function/i;

function inferResearchArea(post: BlogPost): ResearchArea | null {
  const tags = new Set(post.tags ?? []);
  const blob = `${post.title} ${post.excerpt ?? ''}`;

  if (tags.has('policy')) {
    return 'Regulatório';
  }
  if (tags.has('medical')) {
    if (tags.has('cultivation')) {
      return CLINICAL_PATTERN.test(blob) ? 'Medicinal' : 'Agronomia';
    }
    return 'Medicinal';
  }
  if (tags.has('cultivation')) {
    return 'Agronomia';
  }
  if (tags.has('textile')) {
    return CONSTRUCTION_PATTERN.test(blob) ? 'Construção' : 'Têxtil';
  }
  return null;
}

/** Resolved area for filtering; prefers explicit API field, then tag heuristics. */
export function resolveResearchArea(post: BlogPost): ResearchArea | null {
  if (post.research_area && RESEARCH_AREAS.includes(post.research_area as ResearchArea)) {
    return post.research_area as ResearchArea;
  }
  return inferResearchArea(post);
}
