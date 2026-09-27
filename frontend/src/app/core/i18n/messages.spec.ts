import { en, ptBR } from './messages';

describe('services copy (issue #52)', () => {
  it('uses Diagnóstico Gratuito for the Serviços CTA button and form title in pt-BR', () => {
    expect(ptBR['services.ctaButton']).toBe('Diagnóstico Gratuito');
    expect(ptBR['services.formTitle']).toBe('Diagnóstico Gratuito');
    expect(ptBR['services.ctaButton']).not.toContain('consultoria');
    expect(ptBR['services.formTitle']).not.toMatch(/Solicitar consultoria/i);
  });

  it('keeps English services CTA keys defined', () => {
    expect(en['services.ctaButton']).toBeTruthy();
    expect(en['services.formTitle']).toBeTruthy();
  });
});

describe('services premium copy (issue #54)', () => {
  const serviceIds = [
    'svc-viability',
    'svc-engineering',
    'svc-cultivation',
    'svc-regulatory',
    'svc-implementation',
  ] as const;

  for (const id of serviceIds) {
    it(`defines pt-BR and en premium headline/body for ${id}`, () => {
      const headline = `services.premium.${id}.headline` as keyof typeof ptBR;
      const body = `services.premium.${id}.body` as keyof typeof ptBR;

      expect(ptBR[headline].length).toBeGreaterThan(10);
      expect(ptBR[body].length).toBeGreaterThan(40);
      expect(en[headline].length).toBeGreaterThan(10);
      expect(en[body].length).toBeGreaterThan(40);
    });
  }
});
