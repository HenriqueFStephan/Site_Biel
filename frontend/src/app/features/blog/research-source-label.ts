import { BlogPost } from '../../core/models';

/** ISO 3166-1 alpha-2 → localized country name for research source labels. */
const COUNTRY_NAMES: Record<string, { pt: string; en: string }> = {
  AU: { pt: 'Austrália', en: 'Australia' },
  BE: { pt: 'Bélgica', en: 'Belgium' },
  BR: { pt: 'Brasil', en: 'Brazil' },
  CA: { pt: 'Canadá', en: 'Canada' },
  CH: { pt: 'Suíça', en: 'Switzerland' },
  CN: { pt: 'China', en: 'China' },
  CZ: { pt: 'República Tcheca', en: 'Czech Republic' },
  DE: { pt: 'Alemanha', en: 'Germany' },
  DK: { pt: 'Dinamarca', en: 'Denmark' },
  ES: { pt: 'Espanha', en: 'Spain' },
  FI: { pt: 'Finlandia', en: 'Finland' },
  FR: { pt: 'França', en: 'France' },
  GB: { pt: 'Reino Unido', en: 'United Kingdom' },
  GR: { pt: 'Grécia', en: 'Greece' },
  HR: { pt: 'Croácia', en: 'Croatia' },
  HU: { pt: 'Hungria', en: 'Hungary' },
  IE: { pt: 'Irlanda', en: 'Ireland' },
  IL: { pt: 'Israel', en: 'Israel' },
  IN: { pt: 'Índia', en: 'India' },
  IT: { pt: 'Itália', en: 'Italy' },
  JP: { pt: 'Japão', en: 'Japan' },
  KR: { pt: 'Coreia do Sul', en: 'South Korea' },
  LT: { pt: 'Lituânia', en: 'Lithuania' },
  MA: { pt: 'Marrocos', en: 'Morocco' },
  MX: { pt: 'México', en: 'Mexico' },
  NL: { pt: 'Países Baixos', en: 'Netherlands' },
  NO: { pt: 'Noruega', en: 'Norway' },
  NZ: { pt: 'Nova Zelândia', en: 'New Zealand' },
  PL: { pt: 'Polônia', en: 'Poland' },
  PT: { pt: 'Portugal', en: 'Portugal' },
  SE: { pt: 'Suécia', en: 'Sweden' },
  SG: { pt: 'Singapura', en: 'Singapore' },
  TR: { pt: 'Turquia', en: 'Turkey' },
  US: { pt: 'Estados Unidos', en: 'United States' },
  ZA: { pt: 'África do Sul', en: 'South Africa' },
};

function countryName(code: string | undefined, lang: 'pt-BR' | 'en'): string | null {
  if (!code) {
    return null;
  }
  const entry = COUNTRY_NAMES[code.toUpperCase()];
  if (!entry) {
    return code.toUpperCase();
  }
  return lang === 'en' ? entry.en : entry.pt;
}

/** Institution and country label for agent_research posts, e.g. "Deakin University (Austrália)". */
export function researchSourceLabel(
  post: BlogPost,
  lang: 'pt-BR' | 'en' = 'pt-BR',
): string | null {
  if (post.source_type !== 'agent_research') {
    return null;
  }
  const institution = post.research_institution?.trim();
  const country = countryName(post.research_country_code, lang);
  if (!institution || !country) {
    return null;
  }
  return `${institution} (${country})`;
}
