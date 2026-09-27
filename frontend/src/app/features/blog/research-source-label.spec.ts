import { BlogPost } from '../../core/models';
import { researchSourceLabel } from './research-source-label';

const basePost: BlogPost = {
  id: '1',
  title: 'Study',
  slug: 'study',
  excerpt: '',
  content_markdown: '',
  tags: [],
  source_type: 'agent_research',
  author_name: 'Medi Canopy',
  published_at: '2026-01-01',
  research_institution: 'Universidade de São Paulo',
  research_country_code: 'BR',
};

describe('researchSourceLabel', () => {
  it('formats institution and country in Portuguese', () => {
    expect(researchSourceLabel(basePost, 'pt-BR')).toBe('Universidade de São Paulo (Brasil)');
  });

  it('formats institution and country in English', () => {
    expect(researchSourceLabel(basePost, 'en')).toBe('Universidade de São Paulo (Brazil)');
  });

  it('returns null for non-research posts', () => {
    expect(researchSourceLabel({ ...basePost, source_type: 'manual' }, 'pt-BR')).toBeNull();
  });

  it('returns null when institution metadata is missing', () => {
    expect(researchSourceLabel({ ...basePost, research_institution: undefined }, 'pt-BR')).toBeNull();
  });
});
