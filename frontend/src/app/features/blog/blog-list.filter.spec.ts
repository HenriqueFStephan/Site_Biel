import { BlogPost } from '../../core/models';
import { filterBlogPosts, filterBlogPostsByArea, filterBlogPostsByTitle } from './blog-list.filter';

const samplePosts: BlogPost[] = [
  {
    id: '1',
    title: 'CBD for chronic pain in rheumatoid arthritis',
    slug: 'cbd-arthritis',
    excerpt: 'Summary mentions THC but title does not.',
    content_markdown: '',
    tags: [],
    source_type: 'agent_research',
    author_name: 'Author',
    published_at: '2026-01-01',
    research_area: 'Medicinal',
  },
  {
    id: '2',
    title: 'Cannabis sativa varieties for long fibre production',
    slug: 'cannabis-fibre',
    excerpt: 'CBD appears only here in excerpt.',
    content_markdown: '',
    tags: [],
    source_type: 'agent_research',
    author_name: 'Author',
    published_at: '2026-01-02',
    research_area: 'Têxtil',
  },
  {
    id: '3',
    title: 'Industrial hemp agronomic traits',
    slug: 'hemp-traits',
    excerpt: '',
    content_markdown: '',
    tags: [],
    source_type: 'manual',
    author_name: 'Author',
    published_at: '2026-01-03',
    research_area: 'Agronomia',
  },
];

describe('filterBlogPostsByTitle', () => {
  it('returns all posts when the query is empty', () => {
    expect(filterBlogPostsByTitle(samplePosts, '')).toEqual(samplePosts);
    expect(filterBlogPostsByTitle(samplePosts, '   ')).toEqual(samplePosts);
  });

  it('filters by title substring case-insensitively', () => {
    const results = filterBlogPostsByTitle(samplePosts, 'cbd');
    expect(results.map((post) => post.id)).toEqual(['1']);
  });

  it('matches multi-word phrases in the title only', () => {
    const results = filterBlogPostsByTitle(samplePosts, 'cannabis sativa');
    expect(results.map((post) => post.id)).toEqual(['2']);
  });

  it('does not match excerpt or other fields', () => {
    expect(filterBlogPostsByTitle(samplePosts, 'thc')).toEqual([]);
    expect(filterBlogPostsByTitle(samplePosts, 'Summary')).toEqual([]);
  });
});

describe('filterBlogPostsByArea', () => {
  it('returns all posts when no area is selected', () => {
    expect(filterBlogPostsByArea(samplePosts, '')).toEqual(samplePosts);
  });

  it('filters posts by research_area', () => {
    expect(filterBlogPostsByArea(samplePosts, 'Medicinal').map((p) => p.id)).toEqual(['1']);
    expect(filterBlogPostsByArea(samplePosts, 'Agronomia').map((p) => p.id)).toEqual(['3']);
  });
});

describe('filterBlogPosts', () => {
  it('combines area and title filters', () => {
    const results = filterBlogPosts(samplePosts, 'cannabis', 'Têxtil');
    expect(results.map((p) => p.id)).toEqual(['2']);
  });
});
