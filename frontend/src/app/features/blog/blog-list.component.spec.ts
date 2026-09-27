import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of } from 'rxjs';

import { ApiService } from '../../core/api.service';
import { I18nService } from '../../core/i18n';
import { BlogPost } from '../../core/models';
import { BlogListComponent } from './blog-list.component';

const mockPosts: BlogPost[] = [
  {
    id: '1',
    title: 'CBD clinical trial results',
    slug: 'cbd-trial',
    excerpt: 'THC mentioned in excerpt only',
    content_markdown: '',
    tags: [],
    source_type: 'agent_research',
    author_name: 'Author',
    published_at: '2026-01-01',
    research_institution: 'Lincoln University - Missouri',
    research_country_code: 'US',
    research_area: 'Medicinal',
  },
  {
    id: '2',
    title: 'Industrial hemp yield study',
    slug: 'hemp-yield',
    excerpt: '',
    content_markdown: '',
    tags: [],
    source_type: 'manual',
    author_name: 'Author',
    published_at: '2026-01-02',
    research_area: 'Agronomia',
  },
];

describe('BlogListComponent', () => {
  let fixture: ComponentFixture<BlogListComponent>;
  let api: jasmine.SpyObj<ApiService>;

  beforeEach(async () => {
    api = jasmine.createSpyObj<ApiService>('ApiService', ['getBlogPosts']);
    api.getBlogPosts.and.returnValue(of(mockPosts));

    await TestBed.configureTestingModule({
      imports: [BlogListComponent],
      providers: [{ provide: ApiService, useValue: api }],
    }).compileComponents();

    fixture = TestBed.createComponent(BlogListComponent);
    TestBed.inject(I18nService).setLang('pt-BR');
    fixture.detectChanges();
  });

  it('renders the area filter to the left of the keyword search', () => {
    const header = fixture.nativeElement.querySelector('.blog-page-header');
    const intro = header?.querySelector('.blog-page-header__intro');
    const toolbar = header?.querySelector('.blog-page-header__toolbar');
    const area = toolbar?.querySelector('#blog-area-filter');
    const search = toolbar?.querySelector('#blog-search');

    expect(header).toBeTruthy();
    expect(intro?.querySelector('h1')?.textContent?.trim()).toBe('Ciência & Cannabis');
    expect(area?.tagName).toBe('SELECT');
    expect(search?.getAttribute('type')).toBe('search');
    expect(
      Array.from(toolbar?.children ?? []).indexOf(area?.parentElement as Element),
    ).toBeLessThan(Array.from(toolbar?.children ?? []).indexOf(search?.parentElement as Element));
  });

  it('lists the five research areas on the filter control', () => {
    const select: HTMLSelectElement = fixture.nativeElement.querySelector('#blog-area-filter');
    const labels = Array.from(select.options).slice(1).map((o) => o.textContent?.trim());
    expect(labels).toEqual(['Medicinal', 'Agronomia', 'Construção', 'Têxtil', 'Regulatório']);
  });

  it('filters posts by selected area', () => {
    const select: HTMLSelectElement = fixture.nativeElement.querySelector('#blog-area-filter');
    select.value = 'Medicinal';
    select.dispatchEvent(new Event('change'));
    fixture.detectChanges();

    expect(fixture.nativeElement.querySelectorAll('.news-row').length).toBe(1);
    expect(fixture.nativeElement.querySelector('.col-title')?.textContent?.trim()).toBe(
      'CBD clinical trial results',
    );
  });

  it('filters posts by title in real time', () => {
    const input: HTMLInputElement = fixture.nativeElement.querySelector('#blog-search');
    input.value = 'cbd';
    input.dispatchEvent(new Event('input'));
    fixture.detectChanges();

    const titles = Array.from(fixture.nativeElement.querySelectorAll('.col-title')).map(
      (node: Element) => node.textContent?.trim(),
    );
    expect(titles).toEqual(['CBD clinical trial results']);
  });

  it('shows all posts again when the search is cleared', () => {
    const input: HTMLInputElement = fixture.nativeElement.querySelector('#blog-search');

    input.value = 'cbd';
    input.dispatchEvent(new Event('input'));
    fixture.detectChanges();

    input.value = '';
    input.dispatchEvent(new Event('input'));
    fixture.detectChanges();

    expect(fixture.nativeElement.querySelectorAll('.news-row').length).toBe(2);
  });

  it('shows institution and country instead of the generic research tag', () => {
    const tag = fixture.nativeElement.querySelector('.news-row .tag');
    expect(tag?.textContent?.trim()).toBe('Lincoln University - Missouri (Estados Unidos)');
  });

  it('widens the institution column on Ciência & Cannabis rows', () => {
    const row: HTMLElement | null = fixture.nativeElement.querySelector('.blog-news-rows .news-row');
    expect(row).toBeTruthy();
    expect(getComputedStyle(row!).gridTemplateColumns).toBe('120px 156px 1fr 24px');
  });

  it('shows an empty-state message when no title matches', () => {
    const input: HTMLInputElement = fixture.nativeElement.querySelector('#blog-search');
    input.value = 'inexistente';
    input.dispatchEvent(new Event('input'));
    fixture.detectChanges();

    const empty = fixture.nativeElement.querySelector('.blog-empty');
    expect(empty?.textContent?.trim()).toBe('Nenhum artigo encontrado para a busca.');
    expect(fixture.nativeElement.querySelectorAll('.news-row').length).toBe(0);
  });
});
