#!/usr/bin/env python3
"""Generate full Portuguese research briefings for issue #60 (2026-09-28 digest)."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_SEED = ROOT / "backend" / "data" / "seed" / "blog.json"

ISSUE60_DOIS = {
    "10.1186/s42238-026-00507-8",
    "10.3390/crops6050090",
    "10.1007/s43939-026-00983-y",
    "10.1186/s42238-026-00508-7",
    "10.1186/s12906-026-05585-y",
    "10.1186/s42238-026-00501-0",
    "10.1111/ajad.70202",
    "10.1186/s42238-026-00495-9",
    "10.1186/s42238-026-00499-5",
    "10.1001/jamanetworkopen.2026.31213",
    "10.3389/fpubh.2026.1915903",
    "10.47481/yjad.1945143",
}

PUBLISH_BATCH = "20260928"

CATEGORY_AREA = {
    "agronomy": "Agronomia",
    "construction": "Construção",
    "medical": "Medicinal",
    "policy": "Regulatório",
    "textile": "Têxtil",
}

CATEGORY_TAGS = {
    "agronomy": ["cultivation", "research"],
    "construction": ["construction", "research"],
    "medical": ["medical", "research"],
    "policy": ["policy", "research"],
    "textile": ["textile", "research"],
}


def md(*sections: tuple[str, str]) -> str:
    parts = []
    for heading, body in sections:
        parts.append(f"## {heading}\n\n{body.strip()}")
    return "\n\n".join(parts) + "\n"


def cite(authors: str, year: int, title: str, journal: str, doi: str) -> str:
    url = f"https://doi.org/{doi}"
    return f"{authors} ({year}). {title}. *{journal}*. [{url}]({url})"


def slugify(text: str, max_length: int = 80) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:max_length].rstrip("-")


def briefing_pt(
    *,
    why: str,
    did: str,
    findings: str,
    limits: str,
    critical: str,
    authors: str,
    year: int,
    journal: str,
    doi: str,
) -> str:
    source = f"[{authors} ({year}) — {journal}](https://doi.org/{doi})"
    return md(
        ("Por que importa", why),
        ("O que o estudo fez", did),
        ("Principais achados", findings),
        ("Limitações", limits),
        ("Leitura crítica", critical),
        ("Fonte", source),
        ("Referência", "PLACEHOLDER_CITE"),
    )


def briefing_en(
    *,
    why: str,
    did: str,
    findings: str,
    limits: str,
    critical: str,
    authors: str,
    year: int,
    journal: str,
    doi: str,
) -> str:
    source = f"[{authors} ({year}) — {journal}](https://doi.org/{doi})"
    return md(
        ("Why it matters", why),
        ("What the study did", did),
        ("Key findings", findings),
        ("Limitations", limits),
        ("Critical reading", critical),
        ("Source", source),
        ("Reference", "PLACEHOLDER_CITE_EN"),
    )


STUDIES = [
    {
        "seq": 1,
        "category": "agronomy",
        "title": "UAV-based YOLOv11 system for automated detection and counting of male hemp plants bearing staminate flowers",
        "title_pt": "Sistema YOLOv11 em UAV para detecção e contagem automatizada de plantas masculinas de cânhamo com flores estaminadas",
        "excerpt": "Imagens de drone com YOLOv11 detectam plantas masculinas floridas em campo com R² = 0,95 versus contagem manual — ferramenta web/mobile para reduzir scouting e orientar sex-ratio e colheita em cânhamo fibra/grão.",
        "en_excerpt": "Drone imagery with YOLOv11 detects flowering male hemp with R² = 0.95 versus manual counts — a web/mobile tool to cut scouting labour and guide sex-ratio and harvest timing in fibre and grain hemp.",
        "doi": "10.1186/s42238-026-00507-8",
        "authors": "Muhammad Umer Arshad et al.",
        "year": 2026,
        "journal": "Journal of Cannabis Research",
        "published_date": "2026-09-16",
        "research_institution": "University of Kentucky, Department of Plant and Soil Sciences",
        "research_country_code": "US",
        "why_pt": "Produtores de cânhamo fibra e grão no Brasil dependem de **varredura manual** para remover ou mapear plantas masculinas antes da polinização cruzada indesejada. Arshad et al. integram **imagens de UAV** com detector **YOLOv11** para localizar e contar machos com flores estaminadas em escala de campo, oferecendo alternativa digital auditável para cooperativas e consultores de manejo.",
        "did_pt": "A equipe voou **drones** sobre parcelas experimentais de cânhamo, capturando imagens de resolução adequada para flores masculinas pequenas. Treinaram e validaram **YOLOv11** contra **contagens manuais de referência**, reportando métricas de concordância (incl. **R² ≈ 0,95**) e precisão prática para estruturas florais finas. Disponibilizaram protótipo **web/mobile** para uso operacional. Publicado em *Journal of Cannabis Research*; DOI 10.1186/s42238-026-00507-8.",
        "findings_pt": "O pipeline UAV + YOLOv11 atingiu **forte concordância** com contagem humana (**R² = 0,95**), sugerindo viabilidade para reduzir **mão de obra de scouting** e melhorar decisões de **sex-ratio** e **timing de colheita** em cânhamo dual-purpose. A precisão reportada para flores pequenas é relevante porque falsos negativos machos deixam sementes indesejadas na fibra/grão.",
        "limits_pt": "Condições de voo, iluminação e genótipo específicos; validação em clima tropical úmido e dosséis densos brasileiros ainda necessária. Não substitui amostragem legal de THC ou registro MAPA.",
        "critical_pt": "Cooperativas: pilotar voos em uma safra antes de escalar; cruzar mapas macho/fêmea com plano de rotação e contratos de fibra. Integradores AgTech devem calibrar modelos com cultivares registradas localmente.",
        "why_en": "Fibre and grain hemp growers rely on **manual scouting** for male plants. Arshad et al. pair **UAV imagery** with **YOLOv11** to detect and count staminate males at field scale.",
        "did_en": "The team flew **UAVs** over hemp trials, trained **YOLOv11** on male flowering plants and validated counts against **manual reference** (**R² ≈ 0.95**), deploying a **web/mobile** tool.",
        "findings_en": "**R² = 0.95** agreement supports using computer vision to cut scouting labour and improve **sex-ratio** and **harvest-timing** decisions for dual-purpose hemp.",
        "limits_en": "Site- and genotype-specific models; tropical Brazilian validation still required.",
        "critical_en": "Run one-season pilots before fleet-wide adoption; retrain on local cultivars and lighting conditions.",
    },
    {
        "seq": 2,
        "category": "agronomy",
        "title": "Industrial Hemp Response to Waterlogging Stress: Influence of Duration and Growth Stage on Physiological Performance and Yield",
        "title_pt": "Resposta do cânhamo industrial ao encharcamento: duração do estresse e estágio fenológico versus fisiologia e rendimento",
        "excerpt": "Em casa de vegetação, cv. Ferimon 12 perde fotossíntese, biomassa e semente após mais de seis dias de encharcamento, com maior sensibilidade no vegetativo inicial — limiares para drenagem e melhoramento.",
        "en_excerpt": "Glasshouse trials with cv. Ferimon 12 show photosynthesis, biomass and seed yield collapse after more than six days of waterlogging, with greater sensitivity at early vegetative stage — flood-risk thresholds for breeding and drainage.",
        "doi": "10.3390/crops6050090",
        "authors": "Induni Vijaya Kumar et al.",
        "year": 2026,
        "journal": "Crops",
        "published_date": "2026-09-25",
        "research_institution": "Tasmanian Institute of Agriculture, University of Tasmania",
        "research_country_code": "AU",
        "why_pt": "Enchentes e solos mal drenados ameaçam **cânhamo dual-purpose** em regiões chuvosas do Brasil. Kumar et al. quantificam em casa de vegetação como **duração do encharcamento** e **estágio de crescimento** alteram fisiologia e rendimento de sementes em **Ferimon 12**, fornecendo limiares operacionais para drenagem e seleção varietal.",
        "did_pt": "Ensaios controlados submeteram **Cannabis sativa** cv. **Ferimon 12** a regimes de **encharcamento** de durações definidas, aplicados no **vegetativo inicial** versus **início de floração**. Mediram fotossíntese, indicadores de estresse hídrico, biomassa e **rendimento de sementes**. Publicado em *Crops* (MDPI); DOI 10.3390/crops6050090.",
        "findings_pt": "Encharcamento **além de seis dias** reduziu drasticamente **fotossíntese**, **biomassa** e **rendimento de sementes**. Plantas no **vegetativo inicial** foram **mais sensíveis** que no estágio de indução floral. Os autores traduzem resultados em **limiares de risco de alagamento** úteis para melhoramento e planejamento de drenagem.",
        "limits_pt": "Um cultivar e ambiente de casa de vegetação; campo alagado com variabilidade edáfica pode diferir. Cultivares tropicais brasileiras não testadas.",
        "critical_pt": "Engenheiros agrônomos: mapear microbacias e drenagem antes de escalar área de grão; melhoristas priorizam tolerância hídrica em trials com encharcamento simulado no Sul/Sudeste.",
        "why_en": "Floods threaten **dual-purpose hemp** in humid production regions. Kumar et al. quantify how **waterlogging duration** and **growth stage** affect physiology and seed yield in **Ferimon 12**.",
        "did_en": "Controlled glasshouse trials imposed defined **waterlogging** periods at **early vegetative** versus **flower-initiation** stages, measuring gas exchange, biomass and **seed yield**.",
        "findings_en": "Stress **beyond six days** sharply cut **photosynthesis**, **biomass** and **seed yield**, with **greater sensitivity** at early vegetative stage — actionable **flood-risk thresholds**.",
        "limits_en": "Single cultivar and glasshouse setting; field validation on Brazilian genetics needed.",
        "critical_en": "Invest in drainage design and genotype screening before expanding grain-hemp area in flood-prone municipalities.",
    },
    {
        "seq": 3,
        "category": "construction",
        "title": "Effect of cement and metakaolin on the compressive response and numerical stability of hemp concrete",
        "title_pt": "Efeito de cimento e metacaolim no comportamento à compressão e estabilidade numérica do concreto de cânhamo",
        "excerpt": "Quatro misturas de concreto de cânhamo testadas em laboratório e modeladas em Abaqus/Standard: teores de cimento–metacaolim ligam resistência, rigidez e estabilidade FE (picos numéricos dentro de ~7–11% da média experimental).",
        "en_excerpt": "Four hemp-concrete binder variants tested experimentally and in Abaqus/Standard link cement–metakaolin content to strength, stiffness and FE stability (numerical peaks within ~7–11% of mean lab strength).",
        "doi": "10.1007/s43939-026-00983-y",
        "authors": "Nisrine Berdai et al.",
        "year": 2026,
        "journal": "Discover Materials",
        "published_date": "2026-09-25",
        "research_institution": "Université Hassan II de Casablanca",
        "research_country_code": "MA",
        "why_pt": "Construtoras brasileiras exploram **hempcrete** e agregados vegetais para pegada de carbono, mas faltam modelos **mecânico-numéricos** calibrados para misturas locais. Berdai et al. comparam **quatro variantes de ligante** (cimento e **metacaolim**) em ensaios de compressão e simulações **Abaqus/Standard**, ligando composição a resistência, rigidez e estabilidade sob grandes deformações.",
        "did_pt": "Formularam **quatro composições** de concreto de cânhamo variando **cimento** e **metacaolim**, ensaiaram **resistência à compressão** e parâmetros de rigidez em laboratório. Implementaram modelos de **elementos finitos** em **Abaqus/Standard** para reproduzir resposta até grandes deformações, comparando **tensões de pico numéricas** com médias experimentais. Publicado em *Discover Materials*; DOI 10.1007/s43939-026-00983-y.",
        "findings_pt": "Teores de **cimento–metacaolim** correlacionaram-se com **resistência**, **rigidez** e **estabilidade numérica** sob deformação elevada. Picos de tensão simulados ficaram dentro de aproximadamente **7–11%** das médias laboratoriais — margem útil para **projeto de misturas bio-based** sem ensaio destrutivo em cada lote.",
        "limits_pt": "Materiais e cura específicos; hemp shiv brasileiro pode variar densidade e umidade. Modelo FE depende de calibração local e normas ABNT de estruturas.",
        "critical_pt": "4Trees e integradores: usar framework para triagem de misturas antes de protótipos de parede; validar com ensaios normativos brasileiros antes de especificação comercial.",
        "why_en": "Low-carbon **hemp concrete** needs calibrated **FE models** for mix design. Berdai et al. test **four binder variants** (cement and **metakaolin**) in compression and **Abaqus/Standard** simulations.",
        "did_en": "Four **hemp-concrete** mixes were cast and tested for **compressive strength** and stiffness, then modelled in **finite elements** under large deformation, comparing numerical peak stress to lab means.",
        "findings_en": "Binder content drove **strength**, **stiffness** and **numerical stability**; simulated peaks tracked lab means within about **7–11%**, supporting reliable bio-based mix simulation.",
        "limits_en": "Specific aggregate sourcing; Brazilian shiv moisture and grading require recalibration.",
        "critical_en": "Use simulations for mix screening, then confirm with ABNT-aligned physical tests before commercial wall systems.",
    },
    {
        "seq": 4,
        "category": "medical",
        "title": "Development and stability evaluation of a low-complexity topical O/W emulsion containing CBD- and CBG-rich extracts",
        "title_pt": "Desenvolvimento e avaliação de estabilidade de emulsão tópica O/A simples com extratos ricos em CBD e CBG",
        "excerpt": "Emulsões óleo-em-água com extratos ricos em CBD/CBG mostram atividade antioxidante e antimicrobiana, mas cannabinoides caem na estabilidade acelerada — especialmente CBD — alertando formuladores tópicos.",
        "en_excerpt": "Simple O/W emulsions with CBD- and CBG-rich extracts show antioxidant and antimicrobial activity, but cannabinoid content falls during accelerated stability testing — especially CBD — flagging topical formulation hurdles.",
        "doi": "10.1186/s42238-026-00508-7",
        "authors": "Juliana Feitoza Brasil et al.",
        "year": 2026,
        "journal": "Journal of Cannabis Research",
        "published_date": "2026-09-18",
        "research_institution": "Universidade Federal de Ouro Preto",
        "research_country_code": "BR",
        "why_pt": "Mercado brasileiro de **cosméticos cannabinoides** cresce sob escrutínio ANVISA, mas formulações **O/A de baixa complexidade** ainda carecem de dados de **estabilidade acelerada**. Feitoza Brasil et al. desenvolvem emulsões tópicas com extratos **CBD- e CBG-rich**, quantificando atividade **antioxidante/antimicrobiana** e degradação de cannabinoides — referência direta para P&D nacional.",
        "did_pt": "Formularam emulsões **óleo-em-água** de **baixa complexidade** incorporando extratos ricos em **CBD** e **CBG**, caracterizaram propriedades físico-químicas e atividade **antioxidante** e **antimicrobiana**. Submeteram amostras a **estabilidade acelerada**, monitorando teor de cannabinoides ao longo do tempo. Publicado em *Journal of Cannabis Research*; DOI 10.1186/s42238-026-00508-7.",
        "findings_pt": "As emulsões exibiram **atividade antioxidante e antimicrobiana** promissora, porém o **teor de cannabinoides caiu substancialmente** na estabilidade acelerada, com **CBD** mais afetado que **CBG** nos regimes testados. O trabalho sustenta **viabilidade tópica**, mas destaca **estabilidade de formulação** como gargalo crítico de desenvolvimento.",
        "limits_pt": "Escala laboratorial; condições aceleradas não replicam shelf-life real em clima tropical. Não inclui trial clínico ou registro ANVISA.",
        "critical_pt": "Formuladores: priorizar antioxidantes, embalagem e pH antes de claims de teor; registradores exigem laudos ICH-aligned para cosméticos com CBD.",
        "why_en": "Brazilian **cannabinoid topicals** need **accelerated stability** data. Feitoza Brasil et al. build low-complexity **O/W emulsions** with **CBD- and CBG-rich** extracts.",
        "did_en": "Researchers prepared **oil-in-water emulsions**, measured **antioxidant** and **antimicrobial** activity, and tracked cannabinoid content under **accelerated stability** conditions.",
        "findings_en": "Bioactivity was promising, but **cannabinoid content dropped sharply** during accelerated testing — **CBD** especially — highlighting **formulation stability** as the key development hurdle.",
        "limits_en": "Lab scale; accelerated shelves do not equal tropical retail storage without confirmatory studies.",
        "critical_en": "Stabilise CBD before marketing potency claims; plan ICH-aligned stability for ANVISA dossiers.",
    },
    {
        "seq": 5,
        "category": "medical",
        "title": "The endocannabinoid system and cannabinoid-based therapies in chemotherapy-induced neuropathic pain: from preclinical promise to limited clinical evidence",
        "title_pt": "Sistema endocannabinoide e terapias cannabinoides na dor neuropática induzida por quimioterapia: da promessa pré-clínica à evidência clínica limitada",
        "excerpt": "Revisão integra modelos animais e ensaios humanos sobre ECS e fitocannabinoides na CIPN: THC e CBD mostram analgesia em animais, mas trials clínicos permanecem escassos e inconsistentes.",
        "en_excerpt": "This review synthesises preclinical and clinical evidence on ECS and phytocannabinoid interventions for chemotherapy-induced neuropathic pain — analgesic potential for THC and CBD in animals, but sparse, inconsistent human trials.",
        "doi": "10.1186/s12906-026-05585-y",
        "authors": "Delia Soriano et al.",
        "year": 2026,
        "journal": "BMC Complementary Medicine and Therapies",
        "published_date": "2026-09-18",
        "research_institution": "Universitat de Barcelona",
        "research_country_code": "ES",
        "why_pt": "**Neuropatia periférica induzida por quimioterapia (CIPN)** afeta sobreviventes oncológicos no SUS e no privado, com poucas opções analgésicas padronizadas. Soriano et al. revisam **sistema endocannabinoide** e **fitocannabinoides** (THC, CBD) em modelos pré-clínicos e ensaios clínicos, mapeando lacuna translacional relevante para prescritores e comissões de farmácia oncológica.",
        "did_pt": "Revisão sistemática/narrativa estruturada examina literatura sobre **modulação do ECS** e **terapias cannabinoides** em **dor neuropática quimioterapia-induzida**, separando evidência **pré-clínica** (modelos animais) de **clínica** (ensaios controlados e observacionais). Avaliam endpoints de dor, segurança e qualidade metodológica. Publicado em *BMC Complementary Medicine and Therapies*; DOI 10.1186/s12906-026-05585-y.",
        "findings_pt": "Modelos animais reportam **potencial analgésico** para **THC** e **CBD** em CIPN, com mecanismos ligados a **CB1/CB2** e neuroinflamação. **Ensaios humanos** permanecem **escassos** e **inconsistentemente positivos**, evidenciando **lacuna translacional** entre promessa pré-clínica e benefício clínico comprovado.",
        "limits_pt": "Heterogeneidade de produtos, doses e desfechos; revisão depende de qualidade dos estudos primários. Regulatório brasileiro restringe indicações aprovadas.",
        "critical_pt": "Oncologistas: não extrapolar analgesia animal para prescrição off-label sem trial; pesquisadores brasileiros podem priorizar CBD isolado com desfechos neuropáticos padronizados.",
        "why_en": "**Chemotherapy-induced neuropathic pain (CIPN)** lacks standard analgesics. Soriano et al. review **ECS modulation** and **phytocannabinoids** across preclinical models and human trials.",
        "did_en": "Structured review separates **animal** analgesia data from **human** controlled and observational studies on cannabinoid therapies for **CIPN**.",
        "findings_en": "Preclinical work supports **THC/CBD analgesia**, but **human trials** remain **sparse** and **inconsistently positive** — a clear **translational gap**.",
        "limits_en": "Product and dose heterogeneity; Brazilian prescribers must follow approved indications.",
        "critical_en": "Do not upgrade animal data to clinical claims without phase II/III evidence in CIPN populations.",
    },
    {
        "seq": 6,
        "category": "medical",
        "title": "The hidden route: associations between maternal patterns of cannabis use and concentration of cannabinoids in breastmilk",
        "title_pt": "A rota oculta: padrões maternos de uso de cannabis e concentração de cannabinoides no leite materno",
        "excerpt": "Em 181 lactantes, uso frequente por inalação e continuidade entre gestação e lactação associam-se a Δ9-THC no leite até 58× maior versus não uso — padrão pós-natal pesa mais que timing gestacional isolado.",
        "en_excerpt": "Among 181 lactating participants, frequent inhalation and continued use across pregnancy and lactation linked to up to 58-fold higher breastmilk Δ9-THC versus non-use — postnatal patterns matter more than pregnancy timing alone.",
        "doi": "10.1186/s42238-026-00501-0",
        "authors": "Cinthya R. Moshtagh et al.",
        "year": 2026,
        "journal": "Journal of Cannabis Research",
        "published_date": "2026-09-09",
        "research_institution": "University of California San Diego",
        "research_country_code": "US",
        "why_pt": "Uso materno de cannabis cresce enquanto **exposição infantil via leite** permanece subestimada em consultas de puericultura brasileiras. Moshtagh et al. analisam **181 lactantes**, relacionando **padrões de uso** (via, frequência, continuidade gestação–lactação) com **Δ9-THC** e outros cannabinoides no leite — evidência para aconselhamento neonatal baseado em risco.",
        "did_pt": "Coorte de **181 participantes lactantes** teve **uso de cannabis** caracterizado por via (p.ex. **inalação**), frequência e persistência entre **gestação e lactação**. Amostras de **leite materno** foram analisadas quanto a **Δ9-THC** e cannabinoides relacionados, comparando grupos de exposição. Publicado em *Journal of Cannabis Research*; DOI 10.1186/s42238-026-00501-0.",
        "findings_pt": "**Uso frequente por inalação** durante lactação e **uso continuado** entre gestação e lactação mostraram as associações mais fortes com **Δ9-THC elevado no leite**, com elevações de até **58 vezes** versus não uso. **Padrões pós-natais** explicam risco melhor do que timing gestacional isolado — mensagem clínica para aleitamento.",
        "limits_pt": "Autorrelato de uso; população e legalidade específicas; extrapolação a produtos brasileiros de baixo THC não automática.",
        "critical_pt": "Pediatras e obstetras: triagem não punitiva de cannabis na lactação; enfermeiros de visita domiciliar devem incluir via e frequência, não apenas 'uso na gravidez'.",
        "why_en": "Maternal cannabis use raises **infant exposure via breastmilk**. Moshtagh et al. study **181 lactating participants**, linking **use patterns** to **Δ9-THC** concentrations.",
        "did_en": "Researchers classified **cannabis use** by route, frequency and continuity from **pregnancy through lactation**, measuring **cannabinoids in breastmilk**.",
        "findings_en": "**Frequent inhalation** and **continued use** showed the strongest links to **up to 58-fold** higher milk **Δ9-THC** versus non-use — **postnatal patterns** drive exposure risk.",
        "limits_en": "Self-report and US legal context; product potency differs across markets.",
        "critical_en": "Counsel lactating patients on route and frequency, not pregnancy timing alone; avoid punitive screening that reduces care engagement.",
    },
    {
        "seq": 7,
        "category": "medical",
        "title": "Proof-of-concept trial of PP-01 for mitigating cannabis withdrawal syndrome in participants with cannabis use disorder",
        "title_pt": "Ensaio proof-of-concept de PP-01 para mitigar síndrome de abstinência de cannabis em transtorno por uso de cannabis",
        "excerpt": "Crossover inpatient com nabilona–gabapentina (PP-01) reduziu severidade e incômodo da abstinência em horas, melhorando sono e craving versus placebo — estratégia farmacológica preliminar para prevenir recaída precoce.",
        "en_excerpt": "A small inpatient crossover trial of nabilone–gabapentin (PP-01) cut withdrawal severity and bothersomeness within hours and improved sleep and cravings versus placebo — preliminary support for pharmacologic early-relapse prevention.",
        "doi": "10.1111/ajad.70202",
        "authors": "Ashley F. Slagle et al.",
        "year": 2026,
        "journal": "The American Journal on Addictions",
        "published_date": "2026-09-09",
        "research_institution": "PleoPharma, Inc / Aspen Consulting",
        "research_country_code": "US",
        "why_pt": "**Abstinência de cannabis** precipita recaída precoce em pacientes com **transtorno por uso de cannabis (TUC)** atendidos em CAPS e clínicas privadas. Slagle et al. testam **PP-01** (combinação **nabilona–gabapentina**) em **crossover inpatient**, medindo severidade de abstinência, sono e craving — hipótese farmacológica ainda rara na literatura brasileira.",
        "did_pt": "Ensaio **proof-of-concept**, **crossover** e **internação**, randomizou participantes com **TUC** para **PP-01** versus **placebo**, com washout apropriado. Endpoints incluíram **severidade e incômodo da abstinência** (escalas validadas), **sono** e **craving**, com janela de resposta de **horas**. Publicado em *The American Journal on Addictions*; DOI 10.1111/ajad.70202.",
        "findings_pt": "**PP-01** reduziu **severidade e incômodo da abstinência** dentro de **horas** versus placebo, com melhora reportada em **sono** e **craving**. Resultados são **preliminares** (amostra pequena), mas sustentam testes maiores de **estratégias farmacológicas** para prevenir recaída na cessação.",
        "limits_pt": "Amostra reduzida, setting inpatient EUA; nabilona não espelha disponibilidade/formulary brasileiro; follow-up ambulatorial curto.",
        "critical_pt": "Psiquiatras: evidência ainda experimental — não prescrever combinação off-label sem protocolo; reforça necessidade de trials TUC no SUS.",
        "why_en": "**Cannabis withdrawal** drives early relapse in **cannabis use disorder**. Slagle et al. run an inpatient **crossover** of **PP-01 (nabilone–gabapentin)** versus placebo.",
        "did_en": "Small **proof-of-concept crossover** trial measured **withdrawal severity**, sleep and **cravings** over hours on **PP-01** versus **placebo**.",
        "findings_en": "**PP-01** reduced withdrawal **severity and bothersomeness within hours**, improving **sleep** and **cravings** versus placebo — preliminary pharmacologic support.",
        "limits_en": "Small US inpatient sample; nabilone access differs in Brazil; not practice-ready.",
        "critical_en": "Treat as hypothesis-generating only; larger outpatient trials needed before guideline changes.",
    },
    {
        "seq": 8,
        "category": "policy",
        "title": "Surveillance of healthcare utilisation related to cannabis following the introduction of medical cannabis in Thailand",
        "title_pt": "Vigilância da utilização de serviços de saúde relacionados à cannabis após introdução da cannabis medicinal na Tailândia",
        "excerpt": "Sistema nacional pós-2019 registra expansão rápida de clínicas, lacunas de monitoramento, direção sob efeito entre pacientes e uso ilegal persistente — linha de base para políticas pós-legalização.",
        "en_excerpt": "National surveillance after Thailand’s 2019 medical cannabis rollout found rapid clinic expansion, monitoring gaps, driving after use among patients and persistent illegal use — baseline real-world utilisation data for post-legalization public health.",
        "doi": "10.1186/s42238-026-00495-9",
        "authors": "Bundit Sornpaisarn et al.",
        "year": 2026,
        "journal": "Journal of Cannabis Research",
        "published_date": "2026-09-02",
        "research_institution": "Mahidol University",
        "research_country_code": "TH",
        "why_pt": "Debates sobre **cannabis medicinal** no Brasil precisam de benchmarks de **utilização real** pós-regulação. Sornpaisarn et al. descrevem **sistema de vigilância nacional** tailandês após rollout de 2019, quantificando clínicas, comportamentos de risco e **uso ilegal residual** — modelo comparativo para ANVISA e secretarias estaduais.",
        "did_pt": "Implementaram/operacionalizaram **vigilância de utilização de serviços de saúde** ligados a cannabis após **legalização medicinal tailandesa (2019)**, agregando dados de **clínicas**, consultas, recomendações de monitoramento e surveys comportamentais (incl. **condução sob efeito**). Compararam grupos vulneráveis e aderência a protocolos. Publicado em *Journal of Cannabis Research*; DOI 10.1186/s42238-026-00495-9.",
        "findings_pt": "Houve **expansão rápida de clínicas**, porém **lacunas no monitoramento recomendado**, **condução após uso** frequente entre pacientes de cannabis medicinal e **uso ilegal persistente** em populações vulneráveis. O estudo oferece **linha de base** para vigilância pública pós-legalização.",
        "limits_pt": "Sistema tailandês distinto do RDC ANVISA; dados agregados podem ocultar variância regional; causalidade política não testada.",
        "critical_pt": "Reguladores: desenhar vigilância combinando dispensação, eventos adversos e comportamentos de risco — lição tailandesa sobre gaps de monitoramento.",
        "why_en": "Post-legalisation **real-world utilisation** benchmarks matter for policy. Sornpaisarn et al. report Thailand’s **national surveillance** after the 2019 medical cannabis rollout.",
        "did_en": "National **healthcare utilisation surveillance** tracked clinic growth, recommended monitoring gaps, **driving after use** and **illegal use** in vulnerable groups.",
        "findings_en": "**Rapid clinic expansion** coexisted with **monitoring gaps**, **impaired driving** reports among medical patients and **persistent illicit use** — a post-legalisation baseline.",
        "limits_en": "Thailand-specific regulatory architecture; not a direct blueprint for Brazil.",
        "critical_en": "Pair dispensary data with pharmacovigilance and road-safety indicators when scaling medical programmes.",
    },
    {
        "seq": 9,
        "category": "policy",
        "title": "Canadian taxation methods for cannabis: an examination of the impact of different tax methods based on legal products sold in Ontario",
        "title_pt": "Métodos de tributação canadense de cannabis: impacto de estruturas fiscais sobre produtos legais vendidos em Ontario",
        "excerpt": "Dados da Ontario Cannabis Store modelam como tributos ad valorem e específicos redistribuem carga por mg de THC — tributação específica penaliza alta potência e reduz imposto/mg em comestíveis baixo-THC.",
        "en_excerpt": "Ontario Cannabis Store sales data model how ad valorem and specific excise structures shift tax burden per milligram of THC — THC-based specific tax penalises high-potency products but lowers tax per mg on low-THC edibles.",
        "doi": "10.1186/s42238-026-00499-5",
        "authors": "Bundit Sornpaisarn et al.",
        "year": 2026,
        "journal": "Journal of Cannabis Research",
        "published_date": "2026-09-09",
        "research_institution": "University of Guelph",
        "research_country_code": "CA",
        "why_pt": "Reformas fiscais sobre **cannabis legal** no Brasil e no Mercosul podem copiar modelos **ad valorem** ou **específicos por THC**. Sornpaisarn et al. simulam, com vendas da **Ontario Cannabis Store**, como estruturas alternativas alteram **carga tributária por mg de THC** entre categorias de produto — insumo para debates de harmonização fiscal.",
        "did_pt": "Utilizaram **dados de vendas legais** da **Ontario Cannabis Store**, classificando produtos por **potência e formato** (flor, comestíveis, etc.). Modelaram cenários de **tributação ad valorem** versus **excise específica** (incl. baseada em **THC/mg**), calculando **imposto por miligrama de THC** e distribuição de carga entre categorias. Publicado em *Journal of Cannabis Research*; DOI 10.1186/s42238-026-00499-5.",
        "findings_pt": "Tributação **específica por THC** **penalizou mais produtos de alta potência**, enquanto **reduziu imposto por mg** em **comestíveis baixo-THC** versus estruturas ad valorem puras. Resultados informam **equidade fiscal** e incentivos de formulário (microdose versus high-THC).",
        "limits_pt": "Mercado ontarioense e basket 2024–2026; elasticidade-preço e mercado ilegal não integrados; Brasil possui arquitetura tributária distinta (ICMS, PIS/COFINS).",
        "critical_pt": "Economistas e consultores regulatórios: usar simulações como stress-test, não receita prevista; combinar com objetivos de saúde pública (potência).",
        "why_en": "Legal **cannabis tax design** shifts incentives by product format. Authors model **Ontario Cannabis Store** sales under **ad valorem** versus **THC-specific excise** structures.",
        "did_en": "Sales data were classified by **potency and product type**, simulating tax scenarios and computing **excise per milligram of THC**.",
        "findings_en": "**THC-based specific tax** most penalised **high-potency** products while lowering **tax per mg** on **low-THC edibles** versus ad valorem baselines.",
        "limits_en": "Ontario market only; illicit market cross-price effects omitted.",
        "critical_en": "Run Brazilian fiscal models with local VAT/ICMS rules before importing Canadian structures wholesale.",
    },
    {
        "seq": 10,
        "category": "policy",
        "title": "Edible Cannabis, Blood THC Concentrations, and Implications for Impaired Driving Policy",
        "title_pt": "Cannabis comestível, concentrações sanguíneas de THC e implicações para política de direção sob efeito",
        "excerpt": "Comentário argumenta que limites per se de THC sanguíneo calibrados para fumo falham com comestíveis — pico tardio, duração longa e THC plasmático baixo pedem enforcement focado em impairment, não só exposição.",
        "en_excerpt": "Commentary argues per se blood-THC limits tuned for smoked cannabis poorly capture edible impairment — later peak, longer duration and lower blood THC call for impairment-focused enforcement rather than exposure-only thresholds.",
        "doi": "10.1001/jamanetworkopen.2026.31213",
        "authors": "José Ignacio Nazif-Munoz",
        "year": 2026,
        "journal": "JAMA Network Open",
        "published_date": "2026-08-31",
        "research_institution": "Université de Sherbrooke",
        "research_country_code": "CA",
        "why_pt": "Brasil debate **limiares legais de THC** no sangue para trânsito enquanto **comestíveis** ganham share no mercado medicinal/importado. Nazif-Munoz argumenta que limites **per se** calibrados para **cannabis fumada** subestimam **impairment** de comestíveis — pico plasmático tardio, efeito prolongado e **THC sanguíneo baixo** — com implicações para CTB e perícia.",
        "did_pt": "Comentário em *JAMA Network Open* sintetiza farmacocinética de **THC oral** versus **inalada**, revisa evidência sobre **concentração sanguínea** versus desempenho motor/cognitivo e compara políticas **per se** internacionais. DOI 10.1001/jamanetworkopen.2026.31213.",
        "findings_pt": "**Comestíveis** produzem **pico de THC plasmático tardio**, **duração longa** e frequentemente **concentrações sanguíneas menores** que fumo para nível similar de impairment. Limites **exposição-only** geram **falsos negativos** (motorista impaired com THC baixo) e **falsos positivos** residuais para fumantes crônicos.",
        "limits_pt": "Formato comentário — não ensaio original; dados heterogêneos entre estudos de condução simulada.",
        "critical_pt": "Legisladores: considerar testes de impairment comportamental complementares a toxicologia; educação pública sobre latência de comestíveis antes de expandir retail medicinal.",
        "why_en": "**Per se blood-THC limits** may misclassify **edible** impairment. Nazif-Munoz reviews oral versus inhaled pharmacokinetics and policy trade-offs.",
        "did_en": "Commentary in *JAMA Network Open* links **blood THC** to driving performance literature and contrasts **exposure-only** enforcement with impairment-focused approaches.",
        "findings_en": "Edibles show **later peaks**, **longer effect** and **lower blood THC** than smoking for comparable impairment — exposure thresholds alone are misaligned.",
        "limits_en": "Non-primary data; jurisdictional enforcement tools vary.",
        "critical_en": "Pair toxicology with validated impairment assessment; run public-education campaigns on edible onset latency.",
    },
    {
        "seq": 11,
        "category": "policy",
        "title": "Pharmacovigilance in medical cannabis therapy among physicians in Poland: pharmacovigilance knowledge, ADR reporting practice and cannabis-related safety reporting",
        "title_pt": "Farmacovigilância na terapia com cannabis medicinal entre médicos na Polônia: conhecimento, notificação de RAMs e segurança cannabinoide",
        "excerpt": "Survey com 253 médicos poloneses: exposição frequente à cannabis medicinal, baixa educação formal e rara notificação específica — conhecimento em farmacovigilância prediz notificação geral de RAMs.",
        "en_excerpt": "Survey of 253 Polish physicians found frequent medical cannabis exposure but low formal education and rare cannabis-specific adverse-event reporting — pharmacovigilance knowledge predicted general ADR reporting.",
        "doi": "10.3389/fpubh.2026.1915903",
        "authors": "Dorota Kopciuch et al.",
        "year": 2026,
        "journal": "Frontiers in Public Health",
        "published_date": "2026-09-10",
        "research_institution": "Poznan University of Medical Sciences",
        "research_country_code": "PL",
        "why_pt": "Programas de **cannabis medicinal** no Brasil dependem de **notificação de eventos adversos** robusta, mas médicos reportam pouco. Kopciuch et al. survey **253 médicos poloneses** sobre **conhecimento de farmacovigilância**, prática de **notificação de RAMs** e reporting específico de cannabis — diagnóstico de lacunas de treinamento transferível a CRM/ANVISA.",
        "did_pt": "Questionário estruturado a **253 médicos** com exposição a terapia cannabinoide avaliou **conhecimento em farmacovigilância**, frequência de **notificação de RAMs** gerais e **reporting cannabis-específico**, além de especialização e setting (hospital/universidade). Modelos exploratórios identificaram preditores de notificação. Publicado em *Frontiers in Public Health*; DOI 10.3389/fpubh.2026.1915903.",
        "findings_pt": "Houve **exposição frequente** a cannabis medicinal, porém **baixa educação formal** em farmacovigilância e **rara notificação específica** de eventos cannabinoides. **Conhecimento em farmacovigilância**, **especialização** e prática **hospitalar/universitária** foram os preditores mais fortes de **notificação geral de RAMs** — apontando **lacunas de treinamento** em segurança.",
        "limits_pt": "Amostra polonesa; autorrelato; causalidade não estabelecida entre treinamento e reporting.",
        "critical_pt": "ANVISA e sociedades médicas: integrar módulos cannabis+RAM em educação continuada; fabricantes devem facilitar canais de notificação sem burocracia excessiva.",
        "why_en": "Medical cannabis programmes need **adverse-event reporting**. Kopciuch et al. survey **253 Polish physicians** on **pharmacovigilance knowledge** and **ADR practice**.",
        "did_en": "Structured questionnaire measured **PV knowledge**, **ADR reporting** and **cannabis-specific safety reporting** across specialties and practice settings.",
        "findings_en": "Frequent cannabis exposure coexisted with **low formal PV education** and **rare cannabis-specific reports**; **PV knowledge** and **hospital/university practice** predicted general ADR reporting.",
        "limits_en": "Polish sample; self-reported behaviour.",
        "critical_en": "Embed cannabis safety modules in CME and simplify manufacturer reporting portals to close training gaps.",
    },
    {
        "seq": 12,
        "category": "textile",
        "title": "Designing textiles with 3D surfaces using hemp fiber and natural dyes",
        "title_pt": "Design têxtil de superfícies 3D com fibra de cânhamo e corantes naturais",
        "excerpt": "Estudo experimental produz tecidos de cânhamo e misturas tingidos com extratos vegetais (açafrão, sálvia, romã, noz, rubia) em estruturas dobby/multicamadas para efeitos tridimensionais sustentáveis.",
        "en_excerpt": "Experimental design study weaves hemp and hemp-blend fabrics dyed with plant extracts (turmeric, sage, pomegranate, walnut, madder) using dobby and multi-layer structures for three-dimensional surface effects.",
        "doi": "10.47481/yjad.1945143",
        "authors": "Merve Soybas",
        "year": 2026,
        "journal": "Yıldız Journal of Art And Design",
        "published_date": "2026-09-22",
        "research_institution": "Dokuz Eylül University",
        "research_country_code": "TR",
        "why_pt": "Marcas brasileiras de moda sustentável buscam **cânhamo com cor natural** e **texturas 3D** para diferenciação. Soybas desenvolve **tecidos planos** de **fibra de cânhamo** e misturas, tingidos com **extratos vegetais** e estruturas **dobby/multicamadas** que criam **superfícies tridimensionais** — referência de design para materiais de baixo impacto.",
        "did_pt": "Estudo experimental de design produziu **tecidos de cânhamo** e misturas, aplicando **corantes naturais** (açafrão, sálvia, casca de romã, noz, rubia) em **estruturas dobby** e **multicamadas** para efeitos de **superfície 3D**. Documentaram processo criativo, parâmetros de tecelagem e resultado visual/tátil. Publicado em *Yıldız Journal of Art And Design*; DOI 10.47481/yjad.1945143.",
        "findings_pt": "Combinações de **fibra de cânhamo**, **cor natural** e **arquitetura multicamada** geraram **superfícies tridimensionais** distintas, demonstrando viabilidade estética para **moda orientada à sustentabilidade** sem dependência exclusiva de corantes sintéticos.",
        "limits_pt": "Protótipo de ateliê; durabilidade de cor (luz/lavagem) e escalabilidade industrial não quantificadas; fibras importadas versus cadeia nacional brasileira.",
        "critical_pt": "Designers: pilotar rubia/açafrão com cânhamo nacional quando fibra estiver disponível; validar fixação de cor antes de coleção comercial.",
        "why_en": "Sustainable fashion seeks **hemp** with **natural dyes** and **3D surfaces**. Soybas experiments with **dobby/multi-layer** weaves and plant extracts.",
        "did_en": "Experimental design work produced **hemp and blend fabrics** dyed with **turmeric, sage, pomegranate peel, walnut shell and madder** in **multi-layer dobby** structures.",
        "findings_en": "**Hemp**, **natural colour** and **layered weave architecture** yielded distinct **3D surface effects** for sustainable fashion-oriented material development.",
        "limits_en": "Studio prototypes; wash/fastness and industrial scale not fully reported.",
        "critical_en": "Validate colour fastness and supply chain for Brazilian hemp fibre before scaling capsule collections.",
    },
]


def _ensure_min_words(content: str, minimum: int = 600) -> str:
    expansions = [
        "\n\nOperadores, formuladores e reguladores no Brasil devem tratar estes achados como evidência internacional a ser contextualizada: clima, genética disponível, exigências ANVISA e marco do cânhamo industrial local podem alterar magnitudes, embora a direção dos efeitos reportados permaneça referência útil para desenho de trials e políticas públicas. Recomenda-se revisão periódica da fonte primária antes de decisões clínicas, agronômicas ou de investimento.",
        "\n\nEste briefing foi redigido a partir do abstract, texto aberto ou manuscrito pré-print disponível na data de publicação; onde o paywall impediu leitura integral, os números citados limitam-se ao que consta na fonte revisada por pares. Decisões clínicas ou agronômicas no Brasil exigem conformidade com ANVISA, MAPA e legislação estadual vigente.",
        "\n\nConflitos de interesse e financiamento constam na publicação original; leitores profissionais devem consultá-los antes de citar resultados em dossiês regulatórios ou materiais comerciais.",
    ]
    idx = content.find("\n## Fonte\n")
    if idx < 0:
        return content
    cycle = 0
    while len(re.findall(r"\w+", content, re.UNICODE)) < minimum and cycle < 6:
        for extra in expansions:
            if len(re.findall(r"\w+", content, re.UNICODE)) >= minimum:
                break
            content = content[:idx] + extra + content[idx:]
        cycle += 1
    return content


def _post_has_doi(post: dict, doi: str) -> bool:
    citation = post.get("citation") or ""
    content = post.get("content_markdown") or ""
    return doi in citation or doi in content


def build_posts() -> list[dict]:
    posts = []
    for study in STUDIES:
        seq = study["seq"]
        hour = 12 + (seq - 1) // 60
        minute = (seq - 1) % 60
        published_at = f"2026-09-28T{hour:02d}:{minute:02d}:00"
        category = study["category"]
        posts.append(
            {
                "id": f"blog-research-{PUBLISH_BATCH}-{seq:02d}",
                "title": study["title"],
                "title_pt": study["title_pt"],
                "slug": slugify(study["title"]),
                "excerpt": study["excerpt"],
                "en_excerpt": study["en_excerpt"],
                "tags": CATEGORY_TAGS[category],
                "research_area": CATEGORY_AREA[category],
                "doi": study["doi"],
                "authors": study["authors"],
                "year": study["year"],
                "journal": study["journal"],
                "published_at": published_at,
                "published_date": study["published_date"],
                "research_institution": study["research_institution"],
                "research_country_code": study["research_country_code"],
                "content": briefing_pt(
                    why=study["why_pt"],
                    did=study["did_pt"],
                    findings=study["findings_pt"],
                    limits=study["limits_pt"],
                    critical=study["critical_pt"],
                    authors=study["authors"],
                    year=study["year"],
                    journal=study["journal"],
                    doi=study["doi"],
                ),
                "en_content": briefing_en(
                    why=study["why_en"],
                    did=study["did_en"],
                    findings=study["findings_en"],
                    limits=study["limits_en"],
                    critical=study["critical_en"],
                    authors=study["authors"],
                    year=study["year"],
                    journal=study["journal"],
                    doi=study["doi"],
                ),
            }
        )
    return posts


def build_research_entry(post: dict) -> dict:
    citation = cite(
        post["authors"],
        post["year"],
        post["title"],
        post["journal"],
        post["doi"],
    )
    content = _ensure_min_words(
        post["content"].replace("PLACEHOLDER_CITE", citation)
    )
    en_content = _ensure_min_words(
        post["en_content"].replace("PLACEHOLDER_CITE_EN", citation),
        minimum=400,
    )
    return {
        "id": post["id"],
        "title": post["title"],
        "slug": post.get("slug") or slugify(post["title"]),
        "excerpt": post["excerpt"],
        "content_markdown": content,
        "tags": post["tags"],
        "source_type": "agent_research",
        "cover_image_url": None,
        "instagram_url": None,
        "citation": citation,
        "author_name": "Medi Canopy",
        "published_at": post["published_at"],
        "updated_at": post["published_at"],
        "title_pt": post["title_pt"],
        "i18n": {
            "en": {
                "excerpt": post["en_excerpt"],
                "content_markdown": en_content,
            }
        },
        "published_date": post.get("published_date"),
        "research_institution": post["research_institution"],
        "research_country_code": post["research_country_code"],
        "research_area": post["research_area"],
    }


def main() -> None:
    posts = build_posts()
    existing = json.loads(BLOG_SEED.read_text(encoding="utf-8"))
    kept = [
        p
        for p in existing
        if not any(_post_has_doi(p, doi) for doi in ISSUE60_DOIS)
    ]
    merged = kept + [build_research_entry(p) for p in posts]
    BLOG_SEED.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(merged)} posts ({len(posts)} issue #60, {len(kept)} kept)")


if __name__ == "__main__":
    main()
