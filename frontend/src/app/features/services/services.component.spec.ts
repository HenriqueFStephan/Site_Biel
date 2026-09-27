import { readFileSync } from 'node:fs';
import { join } from 'node:path';

import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of, throwError } from 'rxjs';
import { provideRouter } from '@angular/router';

import { ApiService } from '../../core/api.service';
import { I18nService } from '../../core/i18n';
import { ServiceOffering } from '../../core/models';
import { ServicesComponent } from './services.component';

const mockServices: ServiceOffering[] = [
  {
    id: 'svc-viability',
    title: 'Viabilidade & Investimentos',
    description: 'CAPEX • OPEX',
    icon: 'chart',
    highlights: [],
  },
];

describe('ServicesComponent', () => {
  let fixture: ComponentFixture<ServicesComponent>;
  let component: ServicesComponent;
  let i18n: I18nService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ServicesComponent],
      providers: [
        provideRouter([]),
        {
          provide: ApiService,
          useValue: {
            getServices: () => of(mockServices),
          },
        },
      ],
    }).compileComponents();

    i18n = TestBed.inject(I18nService);
    i18n.setLang('pt-BR');
    fixture = TestBed.createComponent(ServicesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('uses a 175% desktop grid track for premium description boxes', () => {
    const scss = readFileSync(join(__dirname, 'services.component.scss'), 'utf8');
    expect(scss).toContain('$service-premium-track-scale: 1.75');
    expect(scss).toMatch(/\$service-premium-track-max \* \$service-premium-track-scale/);
  });

  it('uses +4px font sizes for area titles and topic descriptions', () => {
    const scss = readFileSync(join(__dirname, 'services.component.scss'), 'utf8');
    expect(scss).toContain('font-size: calc(1rem + 4px)');
    expect(scss).toContain('font-size: calc(0.875rem + 4px)');

    const title = fixture.nativeElement.querySelector('.service-row h3') as HTMLElement;
    const topics = fixture.nativeElement.querySelector('.service-row__topics') as HTMLElement;

    expect(parseFloat(getComputedStyle(title).fontSize)).toBe(20);
    expect(parseFloat(getComputedStyle(topics).fontSize)).toBe(18);
  });

  it('renders an orange premium description box beside each service', () => {
    const row = fixture.nativeElement.querySelector('.service-row');
    const premium = row?.querySelector('.service-premium');
    const topics = row?.querySelector('.service-row__topics');

    expect(row).toBeTruthy();
    expect(premium).toBeTruthy();
    expect(topics?.textContent).toContain('CAPEX');
    expect(premium?.textContent).toContain('Transformamos oportunidades');
  });

  it('maps premium copy keys for all five consulting services', () => {
    const ids = [
      'svc-viability',
      'svc-engineering',
      'svc-cultivation',
      'svc-regulatory',
      'svc-implementation',
    ];

    for (const id of ids) {
      expect(component.hasPremiumCopy(id)).withContext(id).toBeTrue();
      expect(component.premiumHeadlineKey(id)).toContain(id);
      expect(component.premiumBodyKey(id)).toContain(id);
    }
  });

  it('shows an error state when services fail to load', () => {
    TestBed.resetTestingModule();
    TestBed.configureTestingModule({
      imports: [ServicesComponent],
      providers: [
        provideRouter([]),
        {
          provide: ApiService,
          useValue: {
            getServices: () => throwError(() => new Error('network')),
          },
        },
      ],
    }).compileComponents();

    const errorFixture = TestBed.createComponent(ServicesComponent);
    errorFixture.detectChanges();

    expect(errorFixture.nativeElement.querySelector('.error-state')).toBeTruthy();
  });
});
