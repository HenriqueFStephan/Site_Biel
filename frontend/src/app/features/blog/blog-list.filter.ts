import { BlogPost } from '../../core/models';
import { ResearchArea, resolveResearchArea } from './research-area';

/** Filters blog posts by title only (case-insensitive substring match). */
export function filterBlogPostsByTitle(posts: BlogPost[], query: string): BlogPost[] {
  const normalized = query.trim().toLowerCase();
  if (!normalized) {
    return posts;
  }
  return posts.filter((post) => post.title.toLowerCase().includes(normalized));
}

/** Filters blog posts by área de atuação when an area is selected. */
export function filterBlogPostsByArea(posts: BlogPost[], area: ResearchArea | ''): BlogPost[] {
  if (!area) {
    return posts;
  }
  return posts.filter((post) => resolveResearchArea(post) === area);
}

/** Applies title search and optional area filter (independent or combined). */
export function filterBlogPosts(
  posts: BlogPost[],
  query: string,
  area: ResearchArea | '',
): BlogPost[] {
  return filterBlogPostsByTitle(filterBlogPostsByArea(posts, area), query);
}
