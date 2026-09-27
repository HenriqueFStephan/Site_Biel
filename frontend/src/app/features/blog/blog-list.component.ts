import { Component, OnDestroy, OnInit } from '@angular/core';
import { CommonModule, DatePipe } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';

import { ApiService } from '../../core/api.service';
import { I18nService, TranslatePipe } from '../../core/i18n';
import { BlogPost } from '../../core/models';
import { filterBlogPosts } from './blog-list.filter';
import { RESEARCH_AREAS, ResearchArea } from './research-area';
import { researchSourceLabel } from './research-source-label';

@Component({
  selector: 'app-blog-list',
  standalone: true,
  imports: [CommonModule, DatePipe, RouterLink, TranslatePipe],
  template: `
    <section class="section">
      <div class="container">
        <header class="page-header blog-page-header">
          <div class="blog-page-header__intro">
            <h1>{{ 'blog.title' | t }}</h1>
            <p>{{ 'blog.lead' | t }}</p>
          </div>
          <div class="blog-page-header__toolbar">
            <div class="blog-page-header__area">
              <label class="visually-hidden" for="blog-area-filter">{{ 'blog.areaFilterLabel' | t }}</label>
              <select
                id="blog-area-filter"
                class="blog-area-filter"
                [value]="selectedArea"
                (change)="onAreaChange($event)"
                [attr.aria-label]="'blog.areaFilterLabel' | t"
              >
                <option value="">{{ 'blog.areaFilterAll' | t }}</option>
                <option *ngFor="let area of researchAreas" [value]="area">{{ area }}</option>
              </select>
            </div>
            <div class="blog-page-header__search">
              <input
                id="blog-search"
                type="search"
                class="blog-search"
                [value]="searchQuery"
                (input)="onSearchInput($event)"
                [placeholder]="'blog.searchPlaceholder' | t"
                [attr.aria-label]="'blog.searchLabel' | t"
                autocomplete="off"
              />
            </div>
          </div>
        </header>

        <div *ngIf="loading" class="loading">{{ 'blog.loading' | t }}</div>
        <div *ngIf="error" class="error-state">{{ error | t }}</div>

        <div class="news-rows blog-news-rows" *ngIf="!loading && !error && filteredPosts.length">
          <a class="news-row" *ngFor="let post of filteredPosts" [routerLink]="['/blog', post.slug]">
            <span class="col-date" *ngIf="displayDate(post) as date">{{ date | date:'d MMM y':undefined:i18n.dateLocale() }}</span>
            <span class="col-tag">
              <span class="tag" *ngIf="researchLabel(post) as label">{{ label }}</span>
            </span>
            <span class="col-title">{{ post.title }}</span>
            <span class="col-arrow">→</span>
          </a>
        </div>

        <p
          *ngIf="!loading && !error && !filteredPosts.length && posts.length"
          class="blog-empty"
          role="status"
        >
          {{ 'blog.noResults' | t }}
        </p>
      </div>
    </section>
  `,
  styleUrls: ['./blog-list.component.scss'],
})
export class BlogListComponent implements OnInit, OnDestroy {
  readonly researchAreas = RESEARCH_AREAS;
  posts: BlogPost[] = [];
  searchQuery = '';
  selectedArea: ResearchArea | '' = '';
  loading = true;
  error: '' | 'blog.error' = '';
  private readonly destroy$ = new Subject<void>();

  constructor(
    private api: ApiService,
    readonly i18n: I18nService,
  ) {}

  get filteredPosts(): BlogPost[] {
    return filterBlogPosts(this.posts, this.searchQuery, this.selectedArea);
  }

  ngOnInit(): void {
    this.load();
    this.i18n.lang$.pipe(takeUntil(this.destroy$)).subscribe(() => this.load());
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  onSearchInput(event: Event): void {
    this.searchQuery = (event.target as HTMLInputElement).value;
  }

  onAreaChange(event: Event): void {
    this.selectedArea = (event.target as HTMLSelectElement).value as ResearchArea | '';
  }

  researchLabel(post: BlogPost): string | null {
    return researchSourceLabel(post, this.i18n.lang());
  }

  displayDate(post: BlogPost): string | null {
    if (post.published_date) {
      return post.published_date;
    }
    if (post.source_type !== 'agent_research') {
      return post.published_at;
    }
    return null;
  }

  private load(): void {
    this.loading = true;
    this.error = '';
    this.api.getBlogPosts().subscribe({
      next: (data) => {
        this.posts = data;
        this.loading = false;
      },
      error: () => {
        this.error = 'blog.error';
        this.loading = false;
      },
    });
  }
}
