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
