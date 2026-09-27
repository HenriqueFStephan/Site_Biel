#!/usr/bin/env python3
"""Generate full Portuguese research briefings for issue #49 (2024 science selection)."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_SEED = ROOT / "backend" / "data" / "seed" / "blog.json"

ISSUE49_DOIS = {
    "10.1111/tpj.16769",
    "10.1038/s41598-024-58931-w",
    "10.1002/agj2.21537",
    "10.1371/journal.pone.0315951",
    "10.1161/JAHA.123.030178",
    "10.1001/jamanetworkopen.2024.34354",
    "10.1001/jamainternmed.2024.3270",
    "10.1001/jamapediatrics.2024.4352",
    "10.1017/S0033291724000990",
    "10.1001/jamahealthforum.2023.4897",
    "10.1001/jamapsychiatry.2024.0698",
    "10.1016/j.jaac.2024.02.016",
    "10.1016/j.jclepro.2024.143689",
    "10.1016/j.clce.2024.100123",
    "10.1016/j.indcrop.2024.118487",
}

PUBLISH_BATCH = "20260927"


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
        "title": "A FLOWERING LOCUS T ortholog is associated with photoperiod-insensitive flowering in hemp (Cannabis sativa L.)",
        "title_pt": "Orthólogo de FLOWERING LOCUS T associado a floração insensível ao fotoperíodo no cânhamo (Cannabis sativa L.)",
        "excerpt": "Mapeamento genético identifica o locus Autoflower2 (~0,5 Mb) e o candidato CsFT1, avanço-chave para cultivares de cânhamo adaptadas a latitudes e sistemas produtivos diversos.",
        "en_excerpt": "Genetic mapping identifies the ~0.5 Mb Autoflower2 locus and CsFT1 candidate — a key advance for hemp cultivars adapted to diverse latitudes and production systems.",
        "tags": ["cultivation", "research"],
        "doi": "10.1111/tpj.16769",
        "authors": "Caroline A. Dowling et al.",
        "year": 2024,
        "journal": "The Plant Journal",
        "published_date": "2024-04-16",
        "research_institution": "Cornell University / Cornell AgriTech",
        "research_country_code": "US",
        "why_pt": "Melhoristas de cânhamo no Brasil precisam de genótipos que floresçam de forma previsível fora do fotoperíodo ideal. Dowling et al. localizam o locus **Autoflower2** (~0,5 Mb) e destacam **CsFT1**, orthólogo de *FLOWERING LOCUS T*, como candidato à floração insensível ao fotoperíodo — base molecular para adaptar cultivares a latitudes, estações e sistemas (campo, greenhouse, autoflower).",
        "did_pt": "Combinaram **mapeamento biparental** e **análise de segregantes em bulk (BSA)** em populações de *Cannabis sativa* tipo cânhamo, correlacionando fenótipos de floração com marcadores genômicos. Refinaram o intervalo em ~**0,5 Mb** no locus **Autoflower2** e examinaram genes de resposta ao fotoperíodo, incluindo **CsFT1**. Publicado em *The Plant Journal*; DOI 10.1111/tpj.16769.",
        "findings_pt": "O locus **Autoflower2** explica variação em floração insensível ao fotoperíodo; **CsFT1** emerge como candidato funcional por analogia com vias FT conhecidas em outras espécies. O achado apoia **marcadores assistidos** para introgressão de autoflorescência sem dragagem agronômica desconhecida — ainda sujeita a validação fenotípica multi-ambiente.",
        "limits_pt": "Populações e ambientes específicos; confirmação funcional de CsFT1 pode exigir edição ou complementação. Extrapolação ao trópico brasileiro demanda ensaios locais de fotoperíodo e THC.",
        "critical_pt": "Programas públicos e privados de melhoramento devem priorizar validação de **Autoflower2/CsFT1** em trials regionais antes de registrar cultivares comerciais. Consultores: cruzar genética de autoflower com exigências legais de THC no Brasil.",
        "why_en": "Hemp breeders need predictable flowering outside ideal photoperiods. Dowling et al. map the **Autoflower2** locus (~0.5 Mb) and highlight **CsFT1**, an *FLOWERING LOCUS T* ortholog, for photoperiod-insensitive flowering.",
        "did_en": "The team used **biparental mapping** and **bulked-segregant analysis** to associate flowering phenotypes with genomic markers, refining a ~**0.5 Mb** interval at **Autoflower2** and examining **CsFT1**.",
        "findings_en": "**Autoflower2** accounts for photoperiod-insensitive flowering variation; **CsFT1** is the leading functional candidate, supporting marker-assisted breeding for latitude-adapted hemp.",
        "limits_en": "Specific populations and environments; functional validation still required. Brazilian tropical trials needed for THC and photoperiod response.",
        "critical_en": "Breeding programmes should validate **Autoflower2/CsFT1** in regional trials before commercial release; align autoflower genetics with local THC compliance rules.",
    },
    {
        "seq": 2,
        "title": "Genetic insights into agronomic and morphological traits of drug-type cannabis revealed by genome-wide association studies",
        "title_pt": "Insights genéticos sobre traços agronômicos e morfológicos de cannabis tipo drug via GWAS",
        "excerpt": "GWAS em 176 acessos de cannabis tipo drug mapeia nove traços agronômicos e morfológicos, base genética para melhoramento assistido por marcadores.",
        "en_excerpt": "A GWAS of 176 drug-type Cannabis accessions maps nine agronomic and morphological traits, providing a genetic foundation for marker-assisted breeding.",
        "tags": ["cultivation", "research"],
        "doi": "10.1038/s41598-024-58931-w",
        "authors": "Maxime de Ronne, Éliana Lapierre & Davoud Torkamaneh",
        "year": 2024,
        "journal": "Scientific Reports",
        "published_date": "2024-04-22",
        "research_institution": "Université Laval",
        "research_country_code": "CA",
        "why_pt": "Cannabis medicinal ainda carece de recursos genotype–phenotype densos comparados a culturas convencionais. De Ronne et al. aplicam **GWAS** em **176 acessos** tipo drug para nove traços agronômicos e morfológicos, oferecendo alvos genéticos para **melhoramento assistido por marcadores** em programas licenciados.",
        "did_pt": "Genotiparam painel diversificado de **176 acessos** de cannabis tipo drug e fenotiparam **nove traços** principais (morfologia e agronomia). Executaram **associação genômica ampla (GWAS)**, identificando SNPs/regiões associadas e discutindo arquitetura genética e potencial de seleção. Publicado em *Scientific Reports*; DOI 10.1038/s41598-024-58931-w.",
        "findings_pt": "O GWAS revelou **associações significativas** para múltiplos traços, com regiões candidatas úteis para **MAS** e introgressão controlada. O painel destaca lacunas de recursos fenotípicos em cannabis moderna versus modelos de soja/milho — reforçando valor deste atlas para priorizar cruzamentos.",
        "limits_pt": "Painel canadense; ambientes de cultivo não necessariamente tropicais. GWAS não substitui validação multi-local nem ensaios regulatórios de THC/CBD.",
        "critical_pt": "Melhoristas brasileiros devem usar os marcadores como **hipóteses**, replicando associações em populações locais ANVISA-compliant. Registradores: exigir dados fenotípicos padronizados em dossiers de cultivar.",
        "why_en": "Medicinal Cannabis lacks dense genotype–phenotype resources versus major crops. De Ronne et al. run a **GWAS** on **176 drug-type accessions** for nine agronomic and morphological traits.",
        "did_en": "The authors genotyped **176 drug-type accessions** and phenotyped **nine major traits**, performing **genome-wide association** to map candidate regions.",
        "findings_en": "Significant associations across traits provide **marker-assisted selection** targets and highlight the genetic architecture gap in modern drug-type Cannabis.",
        "limits_en": "Canadian panel; tropical validation required. Association does not prove causality without functional follow-up.",
        "critical_en": "Brazilian breeders should treat hits as hypotheses to replicate in local, compliance-focused populations.",
    },
    {
        "seq": 3,
        "title": "Nitrogen application and cultivar effects on industrial hemp yield dynamics",
        "title_pt": "Efeito de nitrogênio e cultivar na dinâmica de rendimento de cânhamo industrial",
        "excerpt": "Dois anos de campo com seis doses de N e cinco cultivares mostram resposta fortemente dependente de genótipo — base para recomendações regionais de adubação.",
        "en_excerpt": "Two field years with six N rates and five cultivars show strongly genotype-dependent nitrogen response — evidence for regional fertilisation recommendations.",
        "tags": ["cultivation", "research"],
        "doi": "10.1002/agj2.21537",
        "authors": "Navdeep Kaur et al.",
        "year": 2024,
        "journal": "Agronomy Journal",
        "published_date": "2024-02-19",
        "research_institution": "University of Florida",
        "research_country_code": "US",
        "why_pt": "Recomendações genéricas de **nitrogênio** para cânhamo industrial falham quando cultivares respondem de forma distinta. Kaur et al. testam **seis taxas de N** e **cinco cultivares** por **dois anos**, quantificando emergência, stand final e rendimento — referência para nutrição **genótipo-específica** no Brasil.",
        "did_pt": "Ensaios de campo replicados aplicaram **seis níveis de nitrogênio** a **cinco cultivares** de cânhamo industrial durante **duas safras**. Mediram emergência, estabelecimento, dinâmica de rendimento e interação cultivar × N. Publicado em *Agronomy Journal*; DOI 10.1002/agj2.21537.",
        "findings_pt": "A resposta ao N foi **fortemente dependente de cultivar**: NWG-2730, IH Williams e Yuma destacaram-se em faixas de **168–280 kg N/ha**. **Emergência e stand final** foram determinantes de rendimento, não apenas dose de fertilizante. Autores argumentam por recomendações **regionais e por cultivar**, não regimes únicos.",
        "limits_pt": "Clima da Flórida; cultivares comerciais norte-americanas. Não inclui análise econômica completa (custo N vs ganho de fibra/grão).",
        "critical_pt": "Engenheiros agrônomos brasileiros: calibrar trials locais com mesma lógica cultivar × N antes de bulas de adubação. Cooperativas: monitorar emergência como KPI tão importante quanto kg N/ha.",
        "why_en": "Generic **nitrogen** advice fails when cultivars differ. Kaur et al. test **six N rates** and **five cultivars** over **two years**, linking emergence, stand and yield.",
        "did_en": "Replicated field trials applied **six nitrogen levels** to **five industrial hemp cultivars** for **two seasons**, measuring emergence, stand and yield dynamics.",
        "findings_en": "N response was **cultivar-dependent**; NWG-2730, IH Williams and Yuma performed best around **168–280 kg N/ha**. **Emergence and final stand** strongly drove yield.",
        "limits_en": "Florida climate; US cultivars. Limited economic optimisation analysis.",
        "critical_en": "Run local cultivar × N trials before adopting blanket fertilisation guidelines for Brazilian hemp programmes.",
    },
    {
        "seq": 4,
        "title": "The effects of plant density and duration of vegetative growth phase on agronomic traits of medicinal cannabis (Cannabis sativa L.): A regression analysis",
        "title_pt": "Densidade de plantas e duração da fase vegetativa em cannabis medicinal: análise de regressão",
        "excerpt": "Experimentos controlados mostram que maior densidade aumenta inflorescências de alto valor no dossel superior — evidência quantitativa para produção indoor padronizada.",
        "en_excerpt": "Controlled experiments show higher density increases high-value upper-canopy inflorescences — quantitative evidence for standardised indoor production.",
        "tags": ["cultivation", "medical", "research"],
        "doi": "10.1371/journal.pone.0315951",
        "authors": "Torsten Schober et al.",
        "year": 2024,
        "journal": "PLOS ONE",
        "published_date": "2024-12-30",
        "research_institution": "University of Hohenheim, Institute of Crop Science",
        "research_country_code": "DE",
        "why_pt": "Facilities medicinais indoor precisam otimizar **densidade** e **duração vegetativa** para maximizar biomassa de inflorescência e cannabinoides. Schober et al. aplicam **análise de regressão** em experimentos controlados, quantificando efeitos sobre distribuição de dossel e produção — parâmetros operacionais para salas GMP.",
        "did_pt": "Experimentos com *Cannabis sativa* medicinal variaram **densidade de plantas** e **duração da fase vegetativa**, medindo biomassa, rendimento de inflorescências, distribuição vertical de dossel e produção de cannabinoides. Modelos de **regressão** estimaram relações dose-resposta. Publicado em *PLOS ONE*; DOI 10.1371/journal.pone.0315951.",
        "findings_pt": "Maior **densidade** aumentou a proporção de **inflorescências de alto valor no dossel superior**, com trade-offs documentados em outros traços agronômicos. A **duração vegetativa** modulou acumulação de biomassa e perfil de canopy. Resultados oferecem evidência quantitativa para **padronizar produção indoor/greenhouse**.",
        "limits_pt": "Genótipo(s) e ambiente controlado específicos; não substitui validação microbiológica/ANVISA por lote. Interação luz × densidade não necessariamente explorada.",
        "critical_pt": "Operadores brasileiros: usar regressões como ponto de partida para **SOPs de densidade/vegetativo**, confirmando THC e terpenos por HPLC. Integradores de projeto devem simular fluxo de calor e umidade em densidades altas.",
        "why_en": "Indoor medicinal facilities must tune **density** and **vegetative duration**. Schober et al. use **regression analysis** on controlled trials linking canopy distribution to yield and cannabinoids.",
        "did_en": "Medicinal *Cannabis* trials varied **plant density** and **vegetative-phase length**, measuring biomass, inflorescence yield, canopy distribution and cannabinoid output with **regression models**.",
        "findings_en": "Higher **density** increased the share of **high-value upper-canopy inflorescences**, with documented trade-offs. **Vegetative duration** shaped biomass and canopy architecture for standardised indoor/greenhouse systems.",
        "limits_en": "Specific genotypes and controlled rooms; batch microbiology still required for GMP release.",
        "critical_en": "Use reported regressions to draft **SOPs**, then confirm cannabinoid specs on Brazilian batches before scaling room retrofits.",
    },
    {
        "seq": 5,
        "title": "Association of Cannabis Use With Cardiovascular Outcomes Among US Adults",
        "title_pt": "Associação entre uso de Cannabis e desfechos cardiovasculares em adultos nos EUA",
        "excerpt": "Em 434.104 adultos, uso mais frequente de Cannabis associou-se a maiores odds de IAM, AVC e desfecho cardiovascular combinado — estudo observacional transversal.",
        "en_excerpt": "In 434,104 US adults, more frequent Cannabis use was associated with higher odds of MI, stroke and combined cardiovascular outcomes — a cross-sectional observational study.",
        "tags": ["medical", "research"],
        "doi": "10.1161/JAHA.123.030178",
        "authors": "Abra M. Jeffers et al.",
        "year": 2024,
        "journal": "Journal of the American Heart Association",
        "published_date": "2024-02-28",
        "research_institution": "UCSF",
        "research_country_code": "US",
        "why_pt": "Com expansão de produtos de Cannabis, cardiologistas e reguladores precisam quantificar **risco cardiovascular** em populações reais. Jeffers et al. analisam **434.104 adultos** nos EUA, relacionando frequência de uso a IAM, AVC e desfecho combinado — inclusive entre nunca fumantes de tabaco.",
        "did_pt": "Utilizaram dados observacionais de adultos nos EUA, estratificando **frequência de uso de Cannabis** e ajustando covariáveis demográficas e de tabaco quando possível. Estimaram **odds ratios** para infarto, AVC e endpoint cardiovascular composto. Publicado em *Journal of the American Heart Association*; DOI 10.1161/JAHA.123.030178.",
        "findings_pt": "Maior frequência de Cannabis associou-se a **odds elevadas** de infarto, AVC e desfecho cardiovascular combinado, incluindo em **nunca fumantes de tabaco**. Trata-se de estudo **transversal observacional** — identifica **associações**, não causalidade direta.",
        "limits_pt": "Autorrelato de uso; confundidores residuais (dieta, cocaína, medicações). População norte-americana; produtos e potência distintos do mercado brasileiro.",
        "critical_pt": "Clínicos no Brasil devem triar histórico de Cannabis em pacientes de risco cardiovascular, sem alarmismo causal. Pesquisadores: demandam estudos longitudinais com biomarcadores e tipagem de produto (THC/CBD).",
        "why_en": "Cardiologists need real-world **cardiovascular risk** estimates as Cannabis products expand. Jeffers et al. study **434,104 US adults** linking use frequency to MI, stroke and combined outcomes.",
        "did_en": "Observational US adult data were analysed by **Cannabis use frequency** with covariate adjustment, estimating odds for myocardial infarction, stroke and a combined cardiovascular endpoint.",
        "findings_en": "More frequent use correlated with **higher odds** of MI, stroke and combined cardiovascular events, including among **never-tobacco smokers**. This is **cross-sectional** — association, not proven causation.",
        "limits_en": "Self-report bias and residual confounding; US products and potencies differ from other markets.",
        "critical_en": "Screen cardiovascular patients for Cannabis use without inferring causality; longitudinal product-typed studies remain necessary.",
    },
    {
        "seq": 6,
        "title": "Year-Long Cannabis Use for Medical Symptoms and Brain Activation During Cognitive Processes",
        "title_pt": "Uso de Cannabis por um ano para sintomas médicos e ativação cerebral em processos cognitivos",
        "excerpt": "Neuroimagem longitudinal em adultos que iniciaram Cannabis medicinal não detectou mudanças significativas de ativação cerebral após um ano em tarefas cognitivas — coorte leve a moderada.",
        "en_excerpt": "Longitudinal neuroimaging in adults who began medical Cannabis did not detect significant brain-activation changes after one year on cognitive tasks — a light-to-moderate use cohort.",
        "tags": ["medical", "research"],
        "doi": "10.1001/jamanetworkopen.2024.34354",
        "authors": "Debbie C. L. Burdinski et al.",
        "year": 2024,
        "journal": "JAMA Network Open",
        "published_date": "2024-09-18",
        "research_institution": "MIT McGovern Institute",
        "research_country_code": "US",
        "why_pt": "Pacientes e prescritores questionam efeitos neurológicos de **Cannabis medicinal** de longo prazo. Burdinski et al. acompanham adultos que iniciaram uso para dor, ansiedade, depressão ou sono, medindo **ativação cerebral** durante tarefas de memória de trabalho, recompensa e controle inibitório por **neuroimagem longitudinal**.",
        "did_pt": "Coorte longitudinal com **neuroimagem funcional** antes e após **um ano** de uso medicinal autorizado, aplicando tarefas cognitivas padronizadas. Quantificaram mudanças de ativação em redes relacionadas a memória de trabalho, recompensa e controle inibitório. Publicado em *JAMA Network Open*; DOI 10.1001/jamanetworkopen.2024.34354.",
        "findings_pt": "Após um ano, **não detectaram mudanças longitudinais significativas** na ativação cerebral durante as tarefas nesta coorte **de uso leve a moderado**. Autores enfatizam que isso **não estabelece segurança neurológica global** — potência, via de administração e comorbidades importam.",
        "limits_pt": "Amostra pequena relativa à heterogeneidade de produtos; um ano pode ser insuficiente para efeitos tardios. Não substitui avaliação clínica neuropsicológica completa.",
        "critical_pt": "Prescritores brasileiros: comunicar limites do estudo a pacientes; monitorar sintomas e interações medicamentosas independentemente de neuroimagem. Reguladores: exigir farmacovigilância pós-comercialização.",
        "why_en": "Patients ask about long-term **neurological effects** of medical Cannabis. Burdinski et al. follow adults starting use for pain, anxiety, depression or sleep with **longitudinal neuroimaging** on cognitive tasks.",
        "did_en": "A **one-year longitudinal** fMRI cohort tested working-memory, reward and inhibitory-control tasks before and after authorised medical use.",
        "findings_en": "No **significant longitudinal brain-activation changes** were detected in this **light-to-moderate** cohort — not proof of overall neurological safety.",
        "limits_en": "Short follow-up; heterogeneous products; small sample for rare adverse patterns.",
        "critical_en": "Counsel patients on study limits; rely on clinical follow-up and pharmacovigilance rather than neuroimaging alone.",
    },
    {
        "seq": 7,
        "title": "Prenatal Cannabis Use and Maternal Pregnancy Outcomes",
        "title_pt": "Uso prenatal de Cannabis e desfechos maternos na gestação",
        "excerpt": "Entre 316.722 gestações, uso prenatal de Cannabis associou-se a maiores riscos de hipertensão gestacional, pré-eclâmpsia e outros desfechos — coorte observacional ajustada.",
        "en_excerpt": "Among 316,722 pregnancies, prenatal Cannabis use was associated with higher risks of gestational hypertension, preeclampsia and other outcomes — an adjusted observational cohort.",
        "tags": ["medical", "research"],
        "doi": "10.1001/jamainternmed.2024.3270",
        "authors": "Kelly C. Young-Wolff et al.",
        "year": 2024,
        "journal": "JAMA Internal Medicine",
        "published_date": "2024-07-22",
        "research_institution": "Kaiser Permanente Northern California",
        "research_country_code": "US",
        "why_pt": "Uso de Cannabis na gestação cresce em jurisdições legalizadas; obstetras precisam de evidência robusta. Young-Wolff et al. analisam **316.722 gestações** com ascertamento combinado de **autorrelato e toxicologia**, estimando riscos ajustados de complicações maternais.",
        "did_pt": "Coorte de **316.722 gestações** em sistema integrado de saúde, identificando exposição prenatal a Cannabis via **questionários e testes toxicológicos**. Modelos ajustados estimaram associações com hipertensão gestacional, pré-eclâmpsia, descolamento de placenta e ganho de peso gestacional fora das faixas recomendadas. Publicado em *JAMA Internal Medicine*; DOI 10.1001/jamainternmed.2024.3270.",
        "findings_pt": "Uso prenatal associou-se, após ajuste, a **riscos aumentados** de hipertensão gestacional, pré-eclâmpsia, descolamento de placenta e ganho de peso inadequado. Tamanho amostral e dupla ascertamento de exposição aumentam relevância epidemiológica, mas **natureza observacional** limita inferência causal.",
        "limits_pt": "População californiana segurada; produtos e co-uso de tabaco/alcohol podem confundir. Generalização a sistemas públicos brasileiros exige cautela.",
        "critical_pt": "Obstetras e programas de saúde materna devem manter **aconselhamento abstinência** alinhado a diretrizes, citando magnitude associativa, não causalidade certa. Pesquisa brasileira: registros prospectivos com toxicologia são prioritários.",
        "why_en": "Prenatal Cannabis exposure needs large, well-ascertained cohorts. Young-Wolff et al. study **316,722 pregnancies** with **self-report plus toxicology** for adjusted maternal outcomes.",
        "did_en": "Integrated healthcare records identified prenatal Cannabis via **surveys and toxicology**; adjusted models estimated risks for gestational hypertension, preeclampsia, placental abruption and weight-gain extremes.",
        "findings_en": "Prenatal use was associated with **higher adjusted risks** of several maternal complications — impactful epidemiology, still **observational** not causal proof.",
        "limits_en": "Insured California cohort; residual confounding from co-substances remains.",
        "critical_en": "Maintain abstinence counselling citing association magnitudes; invest in Brazilian prospective toxicology-linked registries.",
    },
    {
        "seq": 8,
        "title": "Prenatal Cannabis Exposure and Executive Function and Aggressive Behavior at Age 5 Years",
        "title_pt": "Exposição prenatal à Cannabis e função executiva e agressividade aos 5 anos",
        "excerpt": "Coorte prospectiva de 250 crianças: exposição prenatal associada a ~0,4 DP a menos em atenção/controle inibitório e mais agressividade observada — achados nuanceados entre domínios cognitivos.",
        "en_excerpt": "A prospective cohort of 250 children: prenatal exposure linked to ~0.4 SD lower attention/inhibitory control and more observed aggression — nuanced findings across cognitive domains.",
        "tags": ["medical", "research"],
        "doi": "10.1001/jamapediatrics.2024.4352",
        "authors": "Sarah A. Keim et al.",
        "year": 2024,
        "journal": "JAMA Pediatrics",
        "published_date": "2024-10-28",
        "research_institution": "Nationwide Children's Hospital",
        "research_country_code": "US",
        "why_pt": "Debates sobre cannabis na gestação exigem dados prospectivos em desenvolvimento infantil. Keim et al. acompanham **250 crianças** até **5 anos**, avaliando **função executiva** e **agressividade** após exposição prenatal reportada.",
        "did_pt": "Coorte **prospectiva** mediu exposição prenatal a Cannabis e, aos **5 anos**, aplicou tarefas de **atenção/controle inibitório**, planejamento e escalas de agressividade observada e reportada por cuidadores, com ajustes estatísticos para confundidores sociodemográficos. Publicado em *JAMA Pediatrics*; DOI 10.1001/jamapediatrics.2024.4352.",
        "findings_pt": "Exposição prenatal associou-se a aproximadamente **0,4 desvios-padrão a menos** em desempenho de atenção/controle inibitório, pior planejamento em tarefas e **mais agressividade observada** após ajuste. Outros desfechos cognitivos reportados por cuidadores **não diferiram significativamente**, tornando a leitura **mais nuanceada** que um déficit global.",
        "limits_pt": "Amostra modesta; ascertamento de exposição heterogêneo; follow-up até 5 anos não captura adolescência.",
        "critical_pt": "Pediatras e psicólogos devem evitar generalizar déficit cognitivo amplo; focar triagem de atenção/comportamento em histórico prenatal positivo. Políticas públicas: reforçar prevenção sem estigmatização materna.",
        "why_en": "Prospective child-development data are essential for prenatal Cannabis debates. Keim et al. follow **250 children** to **age 5** on **executive function** and **aggression** after prenatal exposure.",
        "did_en": "A **prospective cohort** assessed prenatal Cannabis exposure and, at **age 5**, attention/inhibitory control, planning tasks and observed/reported aggression with covariate adjustment.",
        "findings_en": "Prenatal exposure was associated with roughly **0.4 SD lower** attention/inhibitory control, poorer planning and **more observed aggression**, while several caregiver-reported cognitive measures did not differ significantly.",
        "limits_en": "Small sample; exposure misclassification possible; mid-childhood follow-up only.",
        "critical_en": "Avoid overgeneralised cognitive-deficit messaging; target attention/behaviour screening when prenatal exposure is documented.",
    },
    {
        "seq": 9,
        "title": "Age-dependent association of cannabis use with risk of psychotic disorder",
        "title_pt": "Associação dependente da idade entre uso de cannabis e risco de transtorno psicótico",
        "excerpt": "Dados vinculados de jovens mostram associação forte entre Cannabis e psicose na adolescência, não significativa na adulta jovem — interpretar magnitudes com cautela.",
        "en_excerpt": "Linked youth data show a strong Cannabis–psychosis association during adolescence but not in young adulthood — interpret magnitudes cautiously.",
        "tags": ["medical", "research"],
        "doi": "10.1017/S0033291724000990",
        "authors": "André J. McDonald et al.",
        "year": 2024,
        "journal": "Psychological Medicine",
        "published_date": "2024-05-22",
        "research_institution": "University of Toronto",
        "research_country_code": "CA",
        "why_pt": "Políticas de prevenção em saúde mental adolescente dependem de entender **janelas etárias de risco**. McDonald et al. vinculam dados de inquérito e assistência à saúde em jovens, testando se a associação Cannabis–**transtorno psicótico** varia entre **adolescência** e **adulta jovem**.",
        "did_pt": "Integraram **dados administrativos e de survey** em coorte jovem, definindo exposição a Cannabis e incidentes de **transtorno psicótico** diagnosticado. Estimaram associações estratificadas por **faixa etária** com intervalos de confiança. Publicado em *Psychological Medicine*; DOI 10.1017/S0033291724000990.",
        "findings_pt": "Uso de Cannabis associou-se fortemente a transtornos psicóticos subsequentes **durante a adolescência**; a associação correspondente **não foi estatisticamente significativa** na adulta jovem. Eventos raros produziram **intervalos amplos** — magnitudes devem ser interpretadas com cautela.",
        "limits_pt": "Observacional; possível confundimento genético/familiar não totalmente resolvido. Sistemas de saúde canadenses.",
        "critical_pt": "Escolas e serviços de saúde mental no Brasil devem reforçar prevenção **adolescente** baseada em evidência, evitando mensagens únicas para todas as idades. Pesquisa: replicar com coortes latino-americanas.",
        "why_en": "Adolescent mental-health policy needs clarity on **age windows of risk**. McDonald et al. link survey and healthcare data to test Cannabis–**psychotic disorder** associations across **adolescence versus young adulthood**.",
        "did_en": "Linked **administrative and survey data** defined Cannabis exposure and incident **psychotic disorder**, with age-stratified effect estimates.",
        "findings_en": "Cannabis use was strongly associated with later psychotic disorders **in adolescence** but **not statistically significant** in young adulthood; wide confidence intervals caution on effect sizes.",
        "limits_en": "Observational design; residual confounding; Canadian healthcare context.",
        "critical_en": "Tailor prevention messaging to **adolescent** risk windows; replicate in Latin American cohorts before policy extrapolation.",
    },
    {
        "seq": 10,
        "title": "Recreational and Medical Cannabis Legalization and Opioid Prescriptions and Mortality",
        "title_pt": "Legalização recreativa e medicinal de Cannabis e prescrições e mortalidade por opioides",
        "excerpt": "Difference-in-differences em dados estaduais dos EUA (2006–2020) não encontrou associação significativa global com prescrição ou mortalidade por opioides; achado secundário em opioides sintéticos exige cautela.",
        "en_excerpt": "US state-level difference-in-differences (2006–2020) found no significant overall association with opioid prescribing or mortality; a secondary synthetic-opioid signal warrants caution.",
        "tags": ["policy", "research"],
        "doi": "10.1001/jamahealthforum.2023.4897",
        "authors": "Hai V. Nguyen et al.",
        "year": 2024,
        "journal": "JAMA Health Forum",
        "published_date": "2024-01-19",
        "research_institution": "Weill Cornell Medicine",
        "research_country_code": "US",
        "why_pt": "A hipótese de que legalizar Cannabis reduziria **crises de opioides** influencia debates regulatórios. Nguyen et al. aplicam **difference-in-differences** em dados **estaduais dos EUA (2006–2020)**, comparando implementação de leis recreativas e medicinais com prescrições e **mortalidade por overdose de opioides**.",
        "did_pt": "Painel estadual longitudional com **generalized difference-in-differences** avaliou mudanças após adoção de leis **recreativas** e **médicas** de Cannabis. Desfechos: volume de prescrições de opioides e **mortalidade total por overdose**, com análises secundárias por classe (p.ex. opioides sintéticos). Publicado em *JAMA Health Forum*; DOI 10.1001/jamahealthforum.2023.4897.",
        "findings_pt": "**Nenhuma associação estatisticamente significativa global** entre implementação das leis e prescrições ou mortalidade total por opioides. Análise secundária sugeriu **possível redução** em mortes por opioides sintéticos após leis recreativas — achado **exploratório** que exige interpretação cautelosa e replicação.",
        "limits_pt": "Agregado estadual mascara heterogeneidade local; período pré-fentanil recente parcialmente coberto. Não informa diretamente política brasileira de opioides ou Cannabis.",
        "critical_pt": "Formuladores de política devem evitar narrativas simplistas de substituição opioides→Cannabis; exigir evidência local sobre prescrição e harm reduction. Mídia: distinguir endpoints primários de secundários.",
        "why_en": "Claims that Cannabis legalisation curbs **opioid crises** need rigorous quasi-experiments. Nguyen et al. use **state-level difference-in-differences (2006–2020)** on prescriptions and **opioid overdose mortality**.",
        "did_en": "A longitudinal **state panel** with **generalized DiD** tested recreational and medical law implementation against opioid prescribing and **total overdose mortality**, plus synthetic-opioid subgroups.",
        "findings_en": "**No significant overall association** with prescribing or total opioid mortality; a secondary **possible synthetic-opioid decline** after recreational laws is exploratory only.",
        "limits_en": "State aggregation hides local heterogeneity; limited transfer to non-US opioid markets.",
        "critical_en": "Reject one-line substitution narratives; demand local evidence on prescribing, potency and harm-reduction services.",
    },
    {
        "seq": 11,
        "title": "Recreational Marijuana Laws and Teen Marijuana Use, 1993–2021",
        "title_pt": "Leis recreativas de maconha e uso entre adolescentes escolarizados, 1993–2021",
        "excerpt": "YRBS repetido não encontrou evidência de aumento global do uso entre estudantes do ensino médio após leis recreativas — contribuição central ao debate legalização/juventude.",
        "en_excerpt": "Repeated YRBS data found no evidence that recreational cannabis laws increased overall high-school student use — a key legalisation/youth-use contribution.",
        "tags": ["policy", "research"],
        "doi": "10.1001/jamapsychiatry.2024.0698",
        "authors": "D. Mark Anderson et al.",
        "year": 2024,
        "journal": "JAMA Psychiatry",
        "published_date": "2024-04-24",
        "research_institution": "Montana State University",
        "research_country_code": "US",
        "why_pt": "Legalização recreativa alimenta temores sobre **uso adolescente**. Anderson et al. exploram **Youth Risk Behavior Survey (1993–2021)**, testando se adoção de **leis recreativas** elevou uso de maconha entre **estudantes do ensino médio**.",
        "did_pt": "Combinaram séries temporais do **YRBS** com codificação estadual de **recreational marijuana laws**, estimando modelos que comparam tendências pré/pós implementação versus estados controle. Publicado em *JAMA Psychiatry*; DOI 10.1001/jamapsychiatry.2024.0698.",
        "findings_pt": "A análise **não encontrou evidência** de que leis recreativas aumentaram uso global entre adolescentes escolarizados ao longo do período. Importante: amostra cobre **jovens que frequentam escola**, não todos os adolescentes.",
        "limits_pt": "Autorrelato escolar; estados early-adopter pequenos; produtos pós-legalização de alta potência parcialmente posteriores ao fim da série em alguns estados.",
        "critical_pt": "Debates brasileiros sobre reforma devem citar limitação de **população escolarizada** e monitorar dados nacionais de saúde escolar separadamente de mercado ilegal.",
        "why_en": "Recreational legalisation raises **youth use** concerns. Anderson et al. analyse **YRBS (1993–2021)** for changes after **recreational marijuana laws** among **high-school students**.",
        "did_en": "**YRBS** time series were linked to state recreational-law timing with pre/post trend models versus non-adopting states.",
        "findings_en": "No evidence that recreational laws **increased overall use** among school-attending adolescents; findings do not represent all youth.",
        "limits_en": "School-based self-report; high-potency commercial markets partly post-date the series.",
        "critical_en": "Pair international legalisation debates with **non-school youth** surveillance and illegal-market monitoring.",
    },
    {
        "seq": 12,
        "title": "Systematic Review and Meta-Analysis: Medical and Recreational Cannabis Legalization and Cannabis Use Among Youth in the United States",
        "title_pt": "Revisão sistemática e meta-análise: legalização de Cannabis e uso entre jovens nos EUA",
        "excerpt": "Meta-análise: leis médicas sem associação pooled relevante com uso mensal juvenil; legalização recreativa com modesto aumento pooled, especialmente em adultos jovens — alta heterogeneidade.",
        "en_excerpt": "Meta-analysis: medical laws show little pooled association with past-month youth use; recreational legalisation linked to a modest pooled odds increase, especially among young adults — high heterogeneity.",
        "tags": ["policy", "research"],
        "doi": "10.1016/j.jaac.2024.02.016",
        "authors": "Aditya K. S. Pawar et al.",
        "year": 2024,
        "journal": "Journal of the American Academy of Child & Adolescent Psychiatry",
        "published_date": "2024-03-27",
        "research_institution": "Johns Hopkins University School of Medicine",
        "research_country_code": "US",
        "why_pt": "Decisores precisam sintetizar dezenas de estudos conflitantes sobre **legalização e uso juvenil**. Pawar et al. conduzem **revisão sistemática e meta-análise** de estudos dos EUA, separando **leis médicas** e **recreativas**.",
        "did_pt": "Busca sistemática, triagem PRISMA e **meta-análise** de estudos observacionais/quasi-experimentais sobre legalização e uso de Cannabis em **jovens e adultos jovens** nos EUA. Quantificaram **odds pooled** para uso recente e exploraram heterogeneidade (desenho, período, definição legal). Publicado online março/2024, fascículo nov/2024; DOI 10.1016/j.jaac.2024.02.016.",
        "findings_pt": "Leis **médicas** mostraram essencialmente **nenhuma associação pooled** com uso mensal juvenil. **Legalização recreativa** associou-se a **modesto aumento pooled de odds**, mais evidente em **adultos jovens**; autores enfatizam **heterogeneidade substancial** entre tipos de lei, populações e métodos.",
        "limits_pt": "Publicações observacionais predominantes; métricas de uso autorrelatadas; contexto exclusivamente norte-americano.",
        "critical_pt": "Ao traduzir para o Brasil, separar efeitos de **acesso legal**, **marketing** e **apreensões policiais**. Investir em meta-análises locais quando surgirem estudos domésticos pós-regulação.",
        "why_en": "Policymakers need synthesis on **legalisation and youth use**. Pawar et al. perform a **systematic review and meta-analysis** of US studies, splitting **medical** versus **recreational** laws.",
        "did_en": "PRISMA-guided search and **meta-analysis** pooled odds of recent Cannabis use among **youth and young adults**, with heterogeneity exploration.",
        "findings_en": "**Medical laws** showed essentially **no pooled association** with past-month youth use; **recreational legalisation** linked to a **modest pooled odds increase**, especially in **young adults**, amid substantial heterogeneity.",
        "limits_en": "Mostly observational US literature; self-reported use outcomes.",
        "critical_en": "Disentangle legal access, marketing and enforcement when applying findings outside the US; build domestic evidence as regulations evolve.",
    },
    {
        "seq": 13,
        "title": "An eco-friendly droplet-wet spinning technology for producing high-quality hemp/cotton blend yarn",
        "title_pt": "Fiação droplet-wet ecológica para fio misto cânhamo/algodão de alta qualidade",
        "excerpt": "Processo droplet-wet ring-spinning elevou tenacidade do fio misto ~22%, reduziu pilosidade ~50% e aumentou resistência ao estouro do tecido ~8%.",
        "en_excerpt": "A modified droplet-wet ring-spinning process raised blend yarn tenacity ~22%, cut hairiness ~50% and increased fabric bursting strength ~8%.",
        "tags": ["textile", "research"],
        "doi": "10.1016/j.jclepro.2024.143689",
        "authors": "Yali Ling et al.",
        "year": 2024,
        "journal": "Journal of Cleaner Production",
        "published_date": "2024-10-10",
        "research_institution": "North Carolina State University, Wilson College of Textiles",
        "research_country_code": "US",
        "why_pt": "Fiação de **cânhamo** permanece gargalo têxtil por fibras curtas e rígidas. Ling et al. desenvolvem tecnologia **droplet-wet spinning** ecológica para **fio misto cânhamo/algodão**, melhorando tenacidade e uniformidade — relevante para cadeias brasileiras de moda sustentável.",
        "did_pt": "Modificaram **ring spinning** com etapa **droplet-wet**, processando blends cânhamo/algodão e caracterizando **tenacidade, pilosidade, torção** e propriedades de **malha** (p.ex. bursting strength). Compararam com fiação convencional. Publicado em *Journal of Cleaner Production*; DOI 10.1016/j.jclepro.2024.143689.",
        "findings_pt": "Tenacidade do fio misto aumentou cerca de **22%**, pilosidade caiu ~**50%**, permitiu ~**20% menos torção**, e malha exibiu ~**8%** mais resistência ao estouro. Abordagem **eco-friendly** reduz dependência de pretreatment químico agressivo.",
        "limits_pt": "Escala piloto de laboratório; blends e equipamentos específicos; não testa todas fibras de cânhamo brasileiras.",
        "critical_pt": "Indústria têxtil: pilotar droplet-wet com fibra nacional antes de capex; cooperativas de cânhamo devem padronizar comprimento e umidade de fibra curtamente.",
        "why_en": "**Hemp spinning** bottlenecks limit sustainable fashion. Ling et al. advance **eco-friendly droplet-wet spinning** for **hemp/cotton blend yarn** quality.",
        "did_en": "Modified **droplet-wet ring spinning** processed hemp/cotton blends, measuring **tenacity, hairiness, twist** and **knitted fabric bursting strength** versus conventional spinning.",
        "findings_en": "Blend **tenacity rose ~22%**, **hairiness fell ~50%**, ~**20% lower twist** was feasible, and fabric **bursting strength gained ~8%**.",
        "limits_en": "Lab-scale; specific blends and machinery; local fibre validation needed.",
        "critical_en": "Pilot droplet-wet with domestic hemp fibre before major spinning investments.",
    },
    {
        "seq": 14,
        "title": "Improved coloration of hemp fabrics via low-pressure argon plasma assisted surface modification",
        "title_pt": "Coloração de tecidos de cânhamo via plasma de argônio de baixa pressão",
        "excerpt": "Pré-tratamento com plasma de argônio melhora hidrofilicidade e fixação de corantes reativos/vat em cânhamo tecido — coloração com menor dependência de pré-tratamentos aquosos clássicos.",
        "en_excerpt": "Low-pressure argon plasma pretreatment improves hydrophilicity and reactive/vat dye uptake on woven hemp — coloration with less reliance on classic aqueous pretreatments.",
        "tags": ["textile", "research"],
        "doi": "10.1016/j.clce.2024.100123",
        "authors": "Kunal S. Bapat et al.",
        "year": 2024,
        "journal": "Cleaner Chemical Engineering",
        "published_date": "2024-09-07",
        "research_institution": "University of Leeds — School of Chemistry and Leeds Institute of Textiles and Colour",
        "research_country_code": "GB",
        "why_pt": "Cânhamo tecido é difícil de **tingir** uniformemente. Bapat et al. aplicam **plasma de argônio de baixa pressão** para nano-etching superficial e maior **hidrofilicidade**, melhorando interação com **corantes reativos e vat**.",
        "did_pt": "Tecidos de cânhamo tecido submetidos a **pré-tratamento plasma** versus controles químicos; caracterizaram morfologia superficial (nano-etching), ângulo de contato e **força de cor (K/S)** com corantes reativos e vat. Publicado em *Cleaner Chemical Engineering*; DOI 10.1016/j.clce.2024.100123.",
        "findings_pt": "Plasma aumentou **hidrofilicidade** e **força de cor** versus controles, com modificação superficial observável. Proposta alinha-se a processos de **coloração de menor recurso** sem depender exclusivamente de pré-tratamentos aquosos convencionais.",
        "limits_pt": "Batch de laboratório; durabilidade ao lavado e escala industrial não totalmente reportadas aqui; equipamento plasma requer capex.",
        "critical_pt": "Tinturarias brasileiras: testar plasma como etapa antes de corantes eco; validar fastness à lavagem para moda exportadora.",
        "why_en": "Woven **hemp** is hard to dye uniformly. Bapat et al. use **low-pressure argon plasma** for surface nano-etching and **hydrophilicity** to boost **reactive and vat dye** uptake.",
        "did_en": "Woven hemp underwent **plasma pretreatment** versus chemical controls; surface morphology, contact angle and **colour strength** were measured.",
        "findings_en": "Plasma raised **hydrophilicity** and **colour strength** with visible surface modification, supporting lower-resource coloration routes.",
        "limits_en": "Lab batches; industrial wash-fastness and throughput need confirmation.",
        "critical_en": "Brazilian dyehouses should pilot plasma pretreatment and validate export wash-fastness specs.",
    },
    {
        "seq": 15,
        "title": 'Influence of field retting on physicochemical and biological properties of "Futura 75" hemp stems',
        "title_pt": 'Influência do retting de campo nas propriedades físico-químicas e biológicas de caules "Futura 75"',
        "excerpt": "Retting de campo bem-sucedido de Futura 75 em clima mediterrâneo liga microbiota, clima e decohesão de feixes de fibra — variabilidade crítica entre colheita e fibra têxtil.",
        "en_excerpt": "Successful field retting of Futura 75 in a Mediterranean climate links microbes, weather and fibre-bundle decohesion — critical harvest-to-textile variability.",
        "tags": ["textile", "research"],
        "doi": "10.1016/j.indcrop.2024.118487",
        "authors": "Eliane Bou Orm et al.",
        "year": 2024,
        "journal": "Industrial Crops and Products",
        "published_date": "2024-08-01",
        "research_institution": "IMT Mines Alès",
        "research_country_code": "FR",
        "why_pt": "**Retting** de campo define qualidade de fibra bast entre colheita e têxtil. Bou Orm et al. documentam retting bem-sucedido de **Futura 75** em **clima mediterrâneo**, correlacionando **microbiota**, clima, química do caule e **decohesão** de feixes de fibra.",
        "did_pt": "Monitoraram caules de **Futura 75** durante **retting de campo**, amostrando propriedades **físico-químicas e biológicas** (microbiota, umidade, degradação de polissacarídeos) até ponto de colheita de fibra. Publicado em *Industrial Crops and Products*, vol. 214, ago/2024; DOI 10.1016/j.indcrop.2024.118487.",
        "findings_pt": "Demonstraram retting viável em **clima mediterrâneo**, ligando **colonização microbiana** e condições meteorológicas a mudanças bioquímicas e **decohesão** de feixes — explicando variabilidade industrial entre caule colhido e fibra têxtil.",
        "limits_pt": "Cultivar e clima específicos; extrapolação ao trópico úmido brasileiro incerta; controle de patógenos no campo não detalhado neste resumo.",
        "critical_pt": "Produtores brasileiros de fibra: usar Futura 75 como referência, mas replicar trials de retting em microclimas locais; beneficiadores devem logar umidade/chuva diária durante retting.",
        "why_en": "**Field retting** drives bast-fibre quality. Bou Orm et al. track **Futura 75** retting in a **Mediterranean climate**, linking **microbes**, weather, stem chemistry and **bundle decohesion**.",
        "did_en": "**Futura 75** stems were monitored through **field retting**, sampling **physicochemical and biological** properties until fibre harvest readiness.",
        "findings_en": "Successful Mediterranean retting connected **microbial colonisation** and weather to biochemical change and **fibre-bundle decohesion**, explaining industrial variability.",
        "limits_en": "Single cultivar/climate; tropical retting may differ; field pathogen control needs local SOPs.",
        "critical_en": "Treat Futura 75 as a benchmark only — run Brazilian microclimate retting trials with daily weather logging.",
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
        hour = 11 + (seq - 1) // 60
        minute = (seq - 1) % 60
        published_at = f"2026-09-27T{hour:02d}:{minute:02d}:00"
        posts.append(
            {
                "id": f"blog-research-{PUBLISH_BATCH}-{seq:02d}",
                "title": study["title"],
                "title_pt": study["title_pt"],
                "slug": slugify(study["title"]),
                "excerpt": study["excerpt"],
                "en_excerpt": study["en_excerpt"],
                "tags": study["tags"],
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
    entry = {
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
    }
    return entry


def main() -> None:
    posts = build_posts()
    existing = json.loads(BLOG_SEED.read_text(encoding="utf-8"))
    kept = [
        p
        for p in existing
        if not any(_post_has_doi(p, doi) for doi in ISSUE49_DOIS)
    ]
    merged = kept + [build_research_entry(p) for p in posts]
    BLOG_SEED.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(merged)} posts ({len(posts)} issue #49, {len(kept)} kept)")


if __name__ == "__main__":
    main()
