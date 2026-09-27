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
    description: 'CAPEX • OPEX • Viabilidade • Benchmarking • Cenários de Escala',
    icon: 'chart',
    highlights: [],
  },
  {
    id: 'svc-engineering',
    title: 'Engenharia & Desenvolvimento',
    description:
      'Master Planning • Engenharia Conceitual • Layout • Pré-dimensionamento • Sistemas',
    icon: 'blueprint',
    highlights: [],
  },
  {
    id: 'svc-cultivation',
    title: 'Cultivo & Operações',
    description: 'CEA • Cultivo • Crop Steering • Fertirrigação • IPM • Pós-colheita • SOPs',
    icon: 'plant',
    highlights: [],
  },
  {
    id: 'svc-regulatory',
    title: 'Regulatório & Qualidade',
    description:
      'Compliance • GACP/GMP • Boas Práticas • Gap Analysis • Qualidade • Documentação',
    icon: 'shield',
    highlights: [],
  },
  {
    id: 'svc-implementation',
    title: 'Implantação & Performance',
    description: 'Fornecedores • Compras Técnicas • Comissionamento • Treinamento • Otimização',
    icon: 'cycle',
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

  it('renders service topics as a two-column list without bullet separators', () => {
    const row = fixture.nativeElement.querySelector('.service-row');
    const premium = row?.querySelector('.service-premium');
    const topics = row?.querySelector('.service-row__topics');
    const topicItems = topics?.querySelectorAll('li');

    expect(row).toBeTruthy();
    expect(premium).toBeTruthy();
    expect(topics?.tagName).toBe('UL');
    expect(topicItems?.length).toBe(5);
    expect(topics?.textContent).not.toContain('•');
    expect(topicItems?.[0]?.textContent).toContain('CAPEX');
    expect(topicItems?.[4]?.textContent).toContain('Cenários de Escala');
    expect(premium?.textContent).toContain('Transformamos oportunidades');
  });

  it('parses bullet-separated descriptions for all five consulting services', () => {
    const expectedCounts = [5, 5, 7, 6, 5];
    for (let i = 0; i < mockServices.length; i++) {
      const topics = component.serviceTopics(mockServices[i].description);
      expect(topics.length).withContext(mockServices[i].id).toBe(expectedCounts[i]);
      expect(topics.join(' ')).not.toContain('•');
    }
  });

  it('uses a responsive two-column grid for service topic lists', () => {
    const scss = readFileSync(join(__dirname, 'services.component.scss'), 'utf8');
    expect(scss).toMatch(/\.service-row__topics[\s\S]*grid-template-columns: 1fr 1fr/);
    expect(scss).toMatch(/grid-template-columns: 1fr;/);
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
