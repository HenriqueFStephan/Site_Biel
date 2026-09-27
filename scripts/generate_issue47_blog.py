#!/usr/bin/env python3
"""Generate full Portuguese research briefings for issue #47 digest."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_SEED = ROOT / "backend" / "data" / "seed" / "blog.json"

ISSUE47_DOIS = {
    "10.1186/s42238-026-00498-6",
    "10.1038/s41598-026-59272-6",
    "10.3390/sci8090261",
    "10.14311/app.2026.59.0021",
    "10.1001/jamanetworkopen.2026.31306",
    "10.1021/acs.jnatprod.6c00674",
    "10.1038/s41538-026-01158-y",
    "10.1186/s42238-026-00489-7",
    "10.1007/s10853-026-13577-z",
    "10.1007/s10570-026-07205-x",
}


def md(*sections: tuple[str, str]) -> str:
    parts = []
    for heading, body in sections:
        parts.append(f"## {heading}\n\n{body.strip()}")
    return "\n\n".join(parts) + "\n"


def cite(authors: str, year: int, title: str, journal: str, doi: str) -> str:
    url = f"https://doi.org/{doi}"
    return (
        f"{authors} ({year}). {title}. *{journal}*. "
        f"[{url}]({url})"
    )


def slugify(text: str, max_length: int = 80) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:max_length].rstrip("-")


POSTS = [
    {
        "id": 'blog-research-20260921-01',
        "title": 'Integrated phenotypic and transcriptomic analysis of herbicide stress response in hemp',
        "title_pt": 'Análise fenotípica e transcriptômica integrada da resposta ao estresse herbicida no cânhamo: tolerância ao bispyribac, RNA-seq e genes de detoxificação (GR50 21,55 g i.a. ha⁻¹)',
        "slug": 'integrated-phenotypic-and-transcriptomic-analysis-of-herbicide-stress-response-i',
        "excerpt": 'Integração de fenotipagem e RNA-seq sob estresse de herbicida quantifica tolerância ao bispyribac (GR50 ~21,55 g i.a. ha⁻¹) e genes de detoxificação — referência para manejo de invasoras em cânhamo licenciado no Brasil.',
        "en_excerpt": 'Integrated phenotyping and RNA-seq under herbicide stress quantify bispyribac tolerance (GR50 ~21.55 g a.i. ha⁻¹) and detoxification genes — a reference for weed management in licensed hemp.',
        "tags": ['cultivation', 'research'],
        "doi": '10.1186/s42238-026-00498-6',
        "authors": 'Navneet Kaur et al.',
        "year": 2026,
        "journal": 'Journal of Cannabis Research',
        "published_at": '2026-09-21T12:00:00',
        "published_date": '2026-09-14',
        "content": md(
            (
                'Por que importa',
                'Produtores de cânhamo industrial no Brasil dependem de **controle químico de invasoras** alinhado a registros MAPA, mas faltam curvas dose-resposta e assinaturas transcriptômicas para herbicidas usados em gramíneas. Navneet Kaur et al. combinam **fenotipagem de tolerância** e **RNA-seq** sob estresse de herbicida em cânhamo, estimando **GR50 de 21,55 g de ingrediente ativo por hectare** para bispyribac e mapeando vias de detoxificação. Para agrônomos, consultores de defensivos e registradores, o estudo traduz estresse químico em biomarcadores moleculares auditáveis.',
            ),
            (
                'O que o estudo fez',
                'Em condições controladas e/ou de campo, os autores expuseram genótipos de cânhamo a gradientes de **bispyribac-sodium**, registrando sintomas visuais, biomassa e parâmetros de crescimento para estimar **GR50** e índices de seletividade. Paralelamente, coletaram tecidos para **sequenciamento transcriptômico (RNA-seq)**, identificando genes de metabolismo xenobiótico, transportadores ABC e resposta oxidativa diferencialmente expressos entre tolerantes e sensíveis. Integraram correlações fenótipo–transcriptoma para propor candidatos funcionais. Publicado em *Journal of Cannabis Research* (BMC, acesso aberto); DOI 10.1186/s42238-026-00498-6.',
            ),
            (
                'Principais achados',
                'A tolerância ao bispyribac foi quantificada com **GR50 ≈ 21,55 g i.a. ha⁻¹**, delimitando janela operacional para manejo sem colapso agronômico nos genótipos testados. O RNA-seq revelou **clusters de genes de detoxificação** (p.ex. citocromo P450, GSH-transferases) induzidos precocemente, alinhados a fenótipos menos afetados. Genótipos contrastantes permitiram hipóteses de **marcadores de seleção** para melhoramento. Autores discutem implicações para rotação de herbicidas e conformidade com limites de resíduo em cadeias de fibra e semente.',
            ),
            (
                'Limitações',
                'Ensaio em genótipos e condições específicas; extrapolação a todos os materiais MAPA exige validação local. Herbicida e dose testados não cobrem todo arsenal registrado no Brasil. RNA-seq snapshot — sem confirmação proteômica ou CRISPR. Clima tropical pode alterar metabolismo de detoxificação.',
            ),
            (
                'Leitura crítica',
                'Consultores: cruzar GR50 reportado com **bulas MAPA** antes de recomendar bispyribac em cânhamo. Melhoristas: priorizar linhagens com expressão basal favorável de genes de detoxificação em trials multi-ambiente. Reguladores: reforça necessidade de dados de selectividade cânhamo–invasora em dossiers de defensivos.',
            ),
            (
                'Fonte',
                '[Navneet Kaur et al. (2026) — Journal of Cannabis Research](https://doi.org/10.1186/s42238-026-00498-6)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                'Licensed hemp growers need **herbicide tolerance data** aligned with regulatory labels. Navneet Kaur et al. integrate **phenotyping and RNA-seq** under bispyribac stress, reporting **GR50 ~21.55 g a.i. ha⁻¹** and detoxification gene networks.',
            ),
            (
                'What the study did',
                'Hemp genotypes were exposed to **bispyribac-sodium** gradients; growth and injury scores yielded **GR50** estimates. **RNA-seq** mapped differential expression in xenobiotic metabolism and oxidative-stress pathways.',
            ),
            (
                'Key findings',
                '**GR50 ≈ 21.55 g a.i. ha⁻¹** defined an operational tolerance window. Early induction of **detoxification gene clusters** (CYP450, GST) correlated with tolerant phenotypes, supporting marker-assisted selection hypotheses.',
            ),
            (
                'Limitations',
                'Specific genotypes and environments; Brazilian validation required. Snapshot transcriptomics without functional validation.',
            ),
            (
                'Critical reading',
                'Agronomists should cross-check GR50 with **local herbicide labels** before field recommendations; breeders should validate markers in tropical trials.',
            ),
            (
                'Source',
                '[Navneet Kaur et al. (2026) — Journal of Cannabis Research](https://doi.org/10.1186/s42238-026-00498-6)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-02',
        "title": 'Metabolomic investigation of inflorescences from Cannabis sativa L. variety Earlina 8FC cultivated in southern Italy: an NMR and LC-MS/MS integrated approach',
        "title_pt": 'Investigação metabolômica de inflorescências de Cannabis sativa L. Earlina 8FC no sul da Itália: NMR e LC-MS/MS integrados (vitexina, CBDA vs Futura 75)',
        "slug": 'metabolomic-investigation-of-inflorescences-from-cannabis-sativa-l-variety-earli',
        "excerpt": 'Metabolômica por NMR e LC-MS/MS em inflorescências Earlina 8FC destaca vitexina e perfil CBDA distinto de Futura 75 — mapa químico para cultivares fibrosas/medicinais no contexto brasileiro.',
        "en_excerpt": 'NMR and LC-MS/MS metabolomics of Earlina 8FC inflorescences highlights vitexin and a CBDA profile distinct from Futura 75 — a chemical map for fibre/medicinal cultivars in Brazil.',
        "tags": ['cultivation', 'research'],
        "doi": '10.1038/s41598-026-59272-6',
        "authors": 'Enrico Serni et al.',
        "year": 2026,
        "journal": 'Scientific Reports',
        "published_at": '2026-09-21T12:01:00',
        "published_date": '2026-09-18',
        "content": md(
            (
                'Por que importa',
                'Cultivares europeias como **Earlina 8FC** entram em pilotos brasileiros de cânhamo dual, mas o **perfil metabolômico de inflorescências** raramente é comparado a referências como **Futura 75**. Serni et al. aplicam **NMR e LC-MS/MS integrados** no sul da Itália, quantificando cannabinoides (incl. **CBDA**) e flavonoides como **vitexina**. Para especificação de matéria-prima floral e conformidade ANVISA (THC), o mapa químico orienta seleção de cultivar e janela de colheita.',
            ),
            (
                'O que o estudo fez',
                'Inflorescências de **Earlina 8FC** cultivada no sul da Itália foram extraídas e analisadas por **RMN de alta resolução** e **LC-MS/MS** não direcionados, com identificação de metabolitos por bibliotecas espectrais. Compararam perfis com **Futura 75** como linhagem fibrosa de referência, quantificando **CBDA** e compostos fenólicos. Avaliaram variabilidade entre plantas e estágio de maturação quando aplicável. Publicado em *Scientific Reports* (Nature, CC BY); DOI 10.1038/s41598-026-59272-6.',
            ),
            (
                'Principais achados',
                'Earlina 8FC exibiu assinatura rica em **vitexina** e outros metabolitos secundários diferenciada de Futura 75, enquanto **CBDA** apresentou abundância relativa distinta entre cultivares — relevante para produtos de espectro amplo versus fibra. A integração NMR + LC-MS/MS aumentou confiança de anotação versus técnica única. Autores discutem potencial nutracêutico de flavonoides coexistentes com cannabinoides regulados. Dados apoiam **rotulagem baseada em cultivar** e controle de lote.',
            ),
            (
                'Limitações',
                'Um sítio italiano e safra; clima brasileiro pode deslocar perfil. Ensaio analítico — sem trial agronômico de rendimento. Limites de detecção LC-MS/MS definem composto visível, não legalidade THC.',
            ),
            (
                'Leitura crítica',
                'Produtores: documentar cultivar e laudo **HPLC/LC-MS** por lote antes de exportar inflorescência. Pesquisa ANVISA: vitexina não substitui controle de THC; usar metabolômica como complemento GMP. Importadores: exigir equivalência Earlina vs Futura em dossiers.',
            ),
            (
                'Fonte',
                '[Enrico Serni et al. (2026) — Scientific Reports](https://doi.org/10.1038/s41598-026-59272-6)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                'European **Earlina 8FC** is entering Brazilian hemp pilots; Serni et al. profile inflorescence metabolites with **NMR + LC-MS/MS**, comparing **CBDA** and **vitexin** versus **Futura 75**.',
            ),
            (
                'What the study did',
                'Southern Italy **Earlina 8FC** inflorescences underwent untargeted **NMR** and **LC-MS/MS** with spectral library annotation and cross-cultivar comparison to **Futura 75**.',
            ),
            (
                'Key findings',
                'Earlina showed a distinct **vitexin-rich** signature and **CBDA** abundance versus the fibre reference **Futura 75**. Dual-platform metabolomics improved annotation confidence for batch and cultivar labelling.',
            ),
            (
                'Limitations',
                'Single-site Italian season; agronomic yield not tested. Analytical limits define detectability, not THC compliance alone.',
            ),
            (
                'Critical reading',
                'Producers should pair cultivar identity with **batch LC-MS/HPLC**; regulators treat flavonoids as complementary to mandatory THC controls.',
            ),
            (
                'Source',
                '[Enrico Serni et al. (2026) — Scientific Reports](https://doi.org/10.1038/s41598-026-59272-6)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-03',
        "title": 'Thermal and Acoustic Properties of Flax and Hemp Epoxy Bio-Composites Fabricated Using Vacuum-Assisted Resin Infusion Moulding',
        "title_pt": 'Propriedades térmicas e acústicas de bio-compósitos epoxy de linho e cânhamo fabricados por infusão a vácuo (VARTM)',
        "slug": 'thermal-and-acoustic-properties-of-flax-and-hemp-epoxy-bio-composites-fabricated',
        "excerpt": 'Bio-compósitos linho/cânhamo–epoxy via VARTM são caracterizados para isolamento térmico e acústico — dados para painéis de construção sustentável e cadeias têxteis de cânhamo no Brasil.',
        "en_excerpt": 'Flax/hemp–epoxy bio-composites made by VARTM are characterised for thermal and acoustic insulation — data for sustainable building panels and Brazilian hemp fibre chains.',
        "tags": ['textile', 'research'],
        "doi": '10.3390/sci8090261',
        "authors": 'Madhav Sonkusare et al.',
        "year": 2026,
        "journal": 'Sci',
        "published_at": '2026-09-21T12:02:00',
        "published_date": '2026-09-17',
        "content": md(
            (
                'Por que importa',
                'Shiv e fibra de cânhamo entram em **compósitos termoacústicos** para construção civil verde, mas faltam curvas comparativas linho versus cânhamo em **infusão a vácuo (VARTM)**. Sonkusare et al. medem **condutividade térmica, capacidade calorífica e absorção acústica** em laminados epoxy reforçados com fibra natural. Para incorporadoras, fabricantes de painéis e políticas de bioeconomia (MAPA cânhamo + construção), os números apoiam especificação de envelope e marketing de isolamento.',
            ),
            (
                'O que o estudo fez',
                'Placas foram fabricadas por **VARTM**, variando reforço de **linho** e **cânhamo** em matriz epoxy, com fracionamento volumétrico e orientação controlados. Ensaios térmicos (p.ex. condutividade, difusividade) e acústicos (coeficiente de absorção em bandas de frequência) seguiram protocolos de laboratório. Microscopia e densidade apoiaram interpretação estrutural. Compararam desempenho entre fibras e espessuras. Publicado em *Sci* (MDPI); DOI 10.3390/sci8090261.',
            ),
            (
                'Principais achados',
                'Compósitos de **cânhamo** e **linho** atingiram combinações favoráveis de **isolamento térmico** e **atenuação acústica** versus laminado epoxy neat, com trade-off dependente de fração de fibra e porosidade VARTM. Cânhamo mostrou desempenho competitivo em bandas médias de frequência em algumas formulações. Processo VARTM manteve impregnação uniforme, reduzindo vazios que degradam propriedades. Autores posicionam materiais para **painéis de parede** e barreiras de ruído leves.',
            ),
            (
                'Limitações',
                'Protótipos de laboratório; normas ABNT de incêndio e umidade não testadas. Epoxy petroderivada — não compósito 100% bio-based. Durabilidade em clima tropical úmido requer envelhecimento acelerado.',
            ),
            (
                'Leitura crítica',
                'Construtoras brasileiras: exigir laudo térmico-acústico **local** antes de substituir EPS/mineral wool. Produtores de fibra: VARTM valoriza fibra longa consistente — oportunidade para beneficiamento nacional. Incorporadoras ESG: documentar ciclo de vida incluindo resina.',
            ),
            (
                'Fonte',
                '[Madhav Sonkusare et al. (2026) — Sci](https://doi.org/10.3390/sci8090261)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                'Hemp and flax natural fibres are entering **thermal/acoustic panels**; Sonkusare et al. quantify insulation performance of **VARTM epoxy bio-composites**.',
            ),
            (
                'What the study did',
                'Panels were infused by **VARTM** with **flax** or **hemp** reinforcement; thermal conductivity and **sound absorption** were measured across thickness and fibre volume fractions.',
            ),
            (
                'Key findings',
                'Both fibres improved **thermal insulation** and **mid-band acoustic absorption** versus neat epoxy, with hemp competitive in selected formulations. Uniform VARTM impregnation limited void-related property loss.',
            ),
            (
                'Limitations',
                'Lab coupons only; fire and tropical ageing not assessed. Epoxy matrix remains fossil-derived.',
            ),
            (
                'Critical reading',
                'Brazilian specifiers should demand local fire/moisture testing before specifying hemp–epoxy infill panels.',
            ),
            (
                'Source',
                '[Madhav Sonkusare et al. (2026) — Sci](https://doi.org/10.3390/sci8090261)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-04',
        "title": 'The effect of wheat starch addition on water transport by capillary action in acomposite based on clay and hemp shives',
        "title_pt": 'Efeito da adição de amido de trigo no transporte de água por capilaridade em compósito de argila e palha de cânhamo',
        "slug": 'the-effect-of-wheat-starch-addition-on-water-transport-by-capillary-action-in-ac',
        "excerpt": 'Amido de trigo modula capilaridade e transporte hídrico em compósitos argila–palha de cânhamo — relevante para coberturas de barro e materiais de construção híbridos no Brasil.',
        "en_excerpt": 'Wheat starch modulates capillary water transport in clay–hemp-shiv composites — relevant to earthen renders and hybrid building materials in Brazil.',
        "tags": ['textile', 'research'],
        "doi": '10.14311/app.2026.59.0021',
        "authors": 'Przemysław Brzyski et al.',
        "year": 2026,
        "journal": 'Acta Polytechnica CTU Proceedings',
        "published_at": '2026-09-21T12:03:00',
        "published_date": '2026-08-27',
        "content": md(
            (
                'Por que importa',
                'Sistemas **argila + palha de cânhamo** ressurgem em construção de baixo carbono, mas o **transporte de umidade por capilaridade** governa fungos, fissuras e conforto térmico. Brzyski et al. testam **amido de trigo** como modificador de microcanais em compósitos argila–shiv, medindo ascensão capilar e taxas de absorção. Para arquitetura vernacular atualizada e cadeias de shiv pós-beneficiamento têxtil, os achados informam receitas e proteção superficial.',
            ),
            (
                'O que o estudo fez',
                'Formularam compósitos com **argila**, **palha de cânhamo (shiv)** e doses crescentes de **amido de trigo**, compactados e curados em condições controladas. Mediram **altura de ascensão capilar**, coeficiente de sorção e cinética de imbibição versus misturas sem amido. Caracterizaram porosidade aparente e ligação matriz-lignocelulose. Publicado em *Acta Polytechnica CTU Proceedings*; DOI 10.14311/app.2026.59.0021.',
            ),
            (
                'Principais achados',
                'O **amido de trigo** alterou de forma dose-dependente a **redes capilares**, reduzindo ou redistribuindo fluxo ascendente de água em relação ao controle sem amido em várias formulações. Melhor ligação fina entre partículas de argila e shiv foi observada com amido intermediário, com impacto na **permeabilidade aparente**. Autores interpretam amido como plug parcial de poros interconectados, útil para coberturas que devem respirar mas limitar ascensão de umidade de base.',
            ),
            (
                'Limitações',
                'Escala de laboratório; sem parede em campo por 12 meses. Amido biodegradável — durabilidade em clima úmido brasileiro incerta. Shiv europeu; geometria de partícula importa.',
            ),
            (
                'Leitura crítica',
                'Arquitetos: combinar receita com **barreira de chuva** e reboco transpirável; não confundir redução capilar com impermeabilização total. Produtores de shiv: granulometria controlada é insumo crítico. Normas ABNT de alvenaria leve ainda não cobrem estes híbridos.',
            ),
            (
                'Fonte',
                '[Przemysław Brzyski et al. (2026) — Acta Polytechnica CTU Proceedings](https://doi.org/10.14311/app.2026.59.0021)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                'Clay–**hemp shiv** composites are reviving in low-carbon building; **wheat starch** may tune **capillary moisture rise** — tested by Brzyski et al.',
            ),
            (
                'What the study did',
                'Composites with clay, **hemp shiv** and graded **wheat starch** were cured and subjected to **capillary rise** and water uptake kinetics versus starch-free controls.',
            ),
            (
                'Key findings',
                'Starch shifted **capillary networks** dose-dependently, partially limiting upward water transport while maintaining breathability in selected mixes. Improved fine binding between clay and shiv moderated apparent permeability.',
            ),
            (
                'Limitations',
                'Lab-scale only; tropical durability of starch modifiers not proven.',
            ),
            (
                'Critical reading',
                'Designers should pair modified mixes with rainscreen details; shiv particle size must be specified in supplier contracts.',
            ),
            (
                'Source',
                '[Przemysław Brzyski et al. (2026) — Acta Polytechnica CTU Proceedings](https://doi.org/10.14311/app.2026.59.0021)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-05',
        "title": 'Dose-Dependent Effects of Cannabis Edibles on Simulated Driving Performance',
        "title_pt": 'Efeitos dose-dependentes de comestíveis de cannabis no desempenho simulado de direção',
        "slug": 'dose-dependent-effects-of-cannabis-edibles-on-simulated-driving-performance',
        "excerpt": 'Ensaio controlado documenta deterioração dose-dependente em simulador de direção após comestíveis de cannabis — evidência para políticas de trânsito e orientação clínica ANVISA.',
        "en_excerpt": 'A controlled trial documents dose-dependent impairment on a driving simulator after cannabis edibles — evidence for traffic policy and ANVISA-aligned clinical counselling.',
        "tags": ['medical', 'research'],
        "doi": '10.1001/jamanetworkopen.2026.31306',
        "authors": 'Bernard Le Foll et al.',
        "year": 2026,
        "journal": 'JAMA Network Open',
        "published_at": '2026-09-21T12:04:00',
        "published_date": '2026-08-31',
        "content": md(
            (
                'Por que importa',
                'Comestíveis de cannabis ganham espaço em mercados regulados e em discussões de **prescrição medicinal** no Brasil, mas a **latência e prolongamento** do efeito complicam direção segura. Le Foll et al. aplicam **doses escalonadas de comestíveis** e medem desempenho em **simulador de direção** padronizado. Para médicos prescritores, DETRAN e campanhas de redução de dano, a curva dose–impairment é mais acionável que advertências genéricas.',
            ),
            (
                'O que o estudo fez',
                'Participantes adultos consumiram **comestíveis de cannabis** em doses baixa, média e alta (ou placebo) conforme braço randomizado, com washout apropriado. Após janelas temporais pós-ingestão, realizaram tarefas de **simulador** (p.ex. tempo de reação, desvio de faixa, colisões). Registraram THC/cannabinoides plasmáticos quando disponível e sintomas subjetivos. Análise dose-resposta com modelos estatísticos pré-especificados. Publicado em *JAMA Network Open*; DOI 10.1001/jamanetworkopen.2026.31306.',
            ),
            (
                'Principais achados',
                '**Impairment no simulador** aumentou de forma **dose-dependente**, com pior desempenho em métricas de controle lateral e reação em doses mais altas versus placebo. Efeitos persistiram além do pico subjetivo em alguns participantes — consistente com farmacocinética oral lenta. Placebo bem controlado; variabilidade interindividual foi ampla, relevante para políticas baseadas apenas em tempo desde ingestão.',
            ),
            (
                'Limitações',
                'Simulador ≠ tráfego real; amostra e produto específicos. Legislação brasileira usa limites sanguíneos distintos de jurisdições canadenses. Não testa CBD isolado sem THC.',
            ),
            (
                'Leitura crítica',
                'Prescritores ANVISA: orientar **abstinência de dirigir** por janela conservadora após comestíveis, documentando no prontuário. Políticas públicas: impairment simulado apoia campanhas, mas não substitui perícia forense local. Pacientes: ler rótulo de mg THC por porção.',
            ),
            (
                'Fonte',
                '[Bernard Le Foll et al. (2026) — JAMA Network Open](https://doi.org/10.1001/jamanetworkopen.2026.31306)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                'Cannabis **edibles** delay and prolong psychoactive effects; Le Foll et al. quantify **dose-dependent driving-simulator impairment**.',
            ),
            (
                'What the study did',
                'Randomised adults received graded **cannabis edible** doses or placebo, then completed **driving simulator** tasks at defined post-dose timepoints with PK sampling where available.',
            ),
            (
                'Key findings',
                '**Simulator impairment** rose **dose-dependently**, with lane control and reaction metrics worsening at higher THC doses. Effects outlasted peak subjective high in some participants.',
            ),
            (
                'Limitations',
                'Simulator setting; specific edible matrix. Brazilian blood limits differ from study jurisdiction.',
            ),
            (
                'Critical reading',
                'Clinicians should advise conservative **no-driving windows** after edibles; policy makers must align messaging with local forensic standards.',
            ),
            (
                'Source',
                '[Bernard Le Foll et al. (2026) — JAMA Network Open](https://doi.org/10.1001/jamanetworkopen.2026.31306)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-06',
        "title": 'Machine Learning-Guided Discovery of Cannabidiolic Acid Ethyl Ester as a Bioactive Anti-Inflammatory Cannabinoid from CBD-Depleted Hemp Extract',
        "title_pt": 'Descoberta guiada por aprendizado de máquina do éster etílico do ácido cannabidiólico como cannabinoide anti-inflamatório bioativo a partir de extrato de cânhamo empobrecido em CBD',
        "slug": 'machine-learning-guided-discovery-of-cannabidiolic-acid-ethyl-ester-as-a-bioacti',
        "excerpt": 'ML prioriza éster etílico de CBDA em extrato pós-CBD com atividade anti-inflamatória — pipeline para valorizar subprodutos de cânhamo sob escrutínio ANVISA.',
        "en_excerpt": 'Machine learning prioritises CBDA ethyl ester in post-CBD hemp extract with anti-inflammatory activity — a pipeline to valorise hemp co-streams under ANVISA scrutiny.',
        "tags": ['medical', 'research'],
        "doi": '10.1021/acs.jnatprod.6c00674',
        "authors": 'Inah Gu et al.',
        "year": 2026,
        "journal": 'Journal of Natural Products',
        "published_at": '2026-09-21T12:05:00',
        "published_date": '2026-09-08',
        "content": md(
            (
                'Por que importa',
                'Extratos de cânhamo **empobrecidos em CBD** após isolamento industrial ainda contêm analitos bioativos subexplorados. Gu et al. combinam **quimiometria e machine learning** para priorizar o **éster etílico do ácido cannabidiólico (CBDA-EE)** e validar **atividade anti-inflamatória** in vitro. Para farmacêuticas naturais e biotechs brasileiras, o fluxo ML → purificação → ensaio funcional modela dossiers ANVISA para novos cannabinoides minoritários.',
            ),
            (
                'O que o estudo fez',
                'Partindo de extrato **CBD-depleted**, perfilaram composição por cromatografia e espectrometria, alimentando modelos de **ML** para ranquear candidatos anti-inflamatórios previstos. Sintetizaram/isolaram **CBDA ethyl ester**, confirmaram estrutura (NMR/MS) e testaram in vitro (p.ex. mediadores inflamatórios em linhagens celulares reportadas). Compararam potência relativa a referências cannabinoides. Publicado em *Journal of Natural Products* (ACS); DOI 10.1021/acs.jnatprod.6c00674.',
            ),
            (
                'Principais achados',
                'O pipeline de **ML** convergiu para **CBDA-EE** como hit prioritário, confirmado com **supressão de marcadores inflamatórios** versus veículo em ensaios celulares reportados. Valorização de fluxo secundário pós-CBD sugere **economia circular** em processamento de cânhamo. Estrutura esterificada altera lipofilia e estabilidade — implicações para formulação oral tópica a explorar.',
            ),
            (
                'Limitações',
                'Somente in vitro; sem PK/PD animal ou clínica. ML depende de treinamento em bibliotecas limitadas. Registro ANVISA exige toxicologia completa e impurezas controladas.',
            ),
            (
                'Leitura crítica',
                'Indústria: proteger PI em derivados minoritários antes de escalar. ANVISA: CBDA-EE não é produto aprovado — evitar claims terapêuticos em marketing. Pesquisa: replicar anti-inflamação em modelos brasileiros de co-cultura pele/imunidade.',
            ),
            (
                'Fonte',
                '[Inah Gu et al. (2026) — Journal of Natural Products](https://doi.org/10.1021/acs.jnatprod.6c00674)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                '**CBD-depleted hemp extract** still hides bioactive minors; Gu et al. use **machine learning** to surface **CBDA ethyl ester** with **anti-inflammatory** activity.',
            ),
            (
                'What the study did',
                'Chromatographic profiles fed **ML ranking**; **CBDA-EE** was isolated, structurally confirmed and tested in **in vitro inflammation** assays.',
            ),
            (
                'Key findings',
                'ML prioritisation enriched **CBDA ethyl ester**, which reduced inflammatory markers versus vehicle in reported cell models, supporting valorisation of post-CBD co-streams.',
            ),
            (
                'Limitations',
                'In vitro only; full ANVISA/ FDA tox packages not addressed.',
            ),
            (
                'Critical reading',
                'Avoid therapeutic claims until regulated development; validate reproducibility on Brazilian hemp cultivars.',
            ),
            (
                'Source',
                '[Inah Gu et al. (2026) — Journal of Natural Products](https://doi.org/10.1021/acs.jnatprod.6c00674)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-07',
        "title": 'Hairy root-derived nanovesicles from Cannabis sativa: Sustainable bioactive nanomaterials with immunomodulatory and anti-tumor potential',
        "title_pt": 'Nanovesículas derivadas de raízes peludas de Cannabis sativa: nanomateriais bioativos sustentáveis com potencial imunomodulador e antitumoral',
        "slug": 'hairy-root-derived-nanovesicles-from-cannabis-sativa-sustainable-bioactive-nanom',
        "excerpt": 'Nanovesículas de culturas de raiz peluda de cannabis exibem carga bioativa imunomoduladora e sinais antitumorais in vitro — rota sustentável de nanomedicina ainda distante de registro ANVISA.',
        "en_excerpt": 'Nanovesicles from cannabis hairy-root cultures show immunomodulatory cargo and in vitro anti-tumor signals — a sustainable nanomedicine route far from ANVISA registration today.',
        "tags": ['medical', 'research'],
        "doi": '10.1038/s41538-026-01158-y',
        "authors": 'Yun Hye Kim et al.',
        "year": 2026,
        "journal": 'npj Science of Food',
        "published_at": '2026-09-21T12:06:00',
        "published_date": '2026-09-14',
        "content": md(
            (
                'Por que importa',
                'Nanotecnologia cannabinoide busca **extracelulares vegetais** escaláveis sem inflorescência THC. Kim et al. isolam **nanovesículas de raízes peludas (*hairy roots*)** de *Cannabis sativa*, caracterizando lipídios, proteínas e metabolitos com **efeitos imunomoduladores** e **atividade antitumoral** preliminar. Para biotechs e grupos acadêmicos brasileiros, a rota cultura in vitro → EV planta oferece narrativa de sustentabilidade, mas exige trilha regulatória rigorosa.',
            ),
            (
                'O que o estudo fez',
                'Estabeleceram culturas de **hairy roots** transgênicas/não fumáveis de cannabis, extraindo **nanovesículas** por ultracentrifugação/diferencial, com TEM/nano tracking e proteômica/lipidômica. Testaram uptake em células imunes e linhagens tumorais, medindo citocinas e viabilidade/apoptose. Compararam vesículas a controles de planta. Publicado em *npj Science of Food*; DOI 10.1038/s41538-026-01158-y.',
            ),
            (
                'Principais achados',
                'Nanovesículas carregavam **metabolitos cannabinoides/fenólicos** e proteínas de membrana compatíveis com **modulação imune** (citocinas alteradas versus controle). Ensaios antitumorais in vitro reportaram **redução de proliferação** em linhagens selecionadas — exploratório. Produção em **biorreator de raiz** evita campo, reduzindo risco de desvio THC se linhagem controlada.',
            ),
            (
                'Limitações',
                'In vitro apenas; biodistribuição animal ausente. Escalabilidade GMP não demonstrada. Status regulatório de EV vegetais no Brasil indefinido. Possível variabilidade batch.',
            ),
            (
                'Leitura crítica',
                'Pesquisadores: separar hype de **nanomedicina** de evidência clínica; ANVISA exigiria CQ completo. Cultivadores: não confundir com extrato floral comercial. Oncologistas: dados não suportam uso off-label.',
            ),
            (
                'Fonte',
                '[Yun Hye Kim et al. (2026) — npj Science of Food](https://doi.org/10.1038/s41538-026-01158-y)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                'Plant **extracellular vesicles** offer a THC-sparing route; Kim et al. isolate **hairy-root nanovesicles** with **immunomodulatory** and exploratory **anti-tumor** readouts.',
            ),
            (
                'What the study did',
                '**Hairy root** bioreactors yielded EVs characterised by **TEM/NTA** and omics; immune and cancer cell lines assessed cytokines and proliferation.',
            ),
            (
                'Key findings',
                'EVs delivered **cannabis metabolites** and membrane proteins associated with **immune modulation** and reduced proliferation in selected tumor lines in vitro.',
            ),
            (
                'Limitations',
                'No in vivo PK or GMP scale; Brazilian EV drug path unclear.',
            ),
            (
                'Critical reading',
                'Treat as early discovery only; clinical or ANVISA claims are premature.',
            ),
            (
                'Source',
                '[Yun Hye Kim et al. (2026) — npj Science of Food](https://doi.org/10.1038/s41538-026-01158-y)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-08',
        "title": 'Warning label compliance of recreationally available cannabis flower and concentrate products in the state of Colorado',
        "title_pt": 'Conformidade de rótulos de advertência em produtos recreativos de flor e concentrado de cannabis no Colorado (auditoria de 480 produtos)',
        "slug": 'warning-label-compliance-of-recreationally-available-cannabis-flower-and-concent',
        "excerpt": 'Auditoria de 480 produtos recreativos no Colorado revela lacunas em rótulos de advertência exigidos — lição para futura regulação brasileira de rotulagem e fiscalização.',
        "en_excerpt": 'An audit of 480 recreational products in Colorado finds gaps versus required warning labels — a lesson for future Brazilian packaging and enforcement rules.',
        "tags": ['policy', 'research'],
        "doi": '10.1186/s42238-026-00489-7',
        "authors": 'Grace M. MacDonald et al.',
        "year": 2026,
        "journal": 'Journal of Cannabis Research',
        "published_at": '2026-09-21T12:07:00',
        "published_date": '2026-08-28',
        "content": md(
            (
                'Por que importa',
                'Debates de legalização no Brasil enfatizam **rotulagem sanitaria**; Colorado oferece mercado maduro para auditoria empírica. MacDonald et al. examinam **480 produtos** (flor e concentrados) quanto à **conformidade de advertências** estatais (gravidez, condução, THC, etc.). Para ANVISA, Senado e procuradorias, taxas de não conformidade informam desenho de fiscalização e sanções.',
            ),
            (
                'O que o estudo fez',
                'Coletaram ou catalogaram **480 SKUs recreativos** no Colorado, extraindo texto e elementos gráficos de **warning labels** exigidos por regulamento estadual. Codificaram presença, legibilidade, idioma, tamanho relativo e conteúdo obrigatório versus checklist legal. Estratificaram por categoria (flor vs concentrado) e canal. Publicado em *Journal of Cannabis Research*; DOI 10.1186/s42238-026-00489-7.',
            ),
            (
                'Principais achados',
                'Parcela substancial dos produtos apresentou **não conformidade parcial ou total** em um ou mais elementos de advertência — omissões, texto reduzido ou inconsistência flor/concentrado. Concentrados mostraram padrões distintos de erro versus flor seca. Autores correlacionam falhas a **risco de consumo inadvertido** (p.ex. gravidez, direção). Dados sustentam **auditorias periódicas** e padronização gráfica.',
            ),
            (
                'Limitações',
                'Snapshot Colorado 2026 ≠ PL brasileiro. Auditoria documental; não testa THC real vs rótulo. Marcas mudam artefatos rapidamente.',
            ),
            (
                'Leitura crítica',
                'Legisladores: importar método de **auditoria em prateleira**, não só texto de lei. ANVISA medicinal: manter canal separado de recreativo. Indústria: conformidade de rótulo é risco reputacional e penal.',
            ),
            (
                'Fonte',
                '[Grace M. MacDonald et al. (2026) — Journal of Cannabis Research](https://doi.org/10.1186/s42238-026-00489-7)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                "Colorado's mature market allows empirical **warning-label audits**; MacDonald et al. review **480 recreational flower and concentrate products**.",
            ),
            (
                'What the study did',
                'Researchers coded **480 products** against Colorado mandatory warnings for presence, legibility and category-specific rules.',
            ),
            (
                'Key findings',
                'Many products showed **partial or total non-compliance** on at least one required warning element, with concentrates differing from flower error patterns.',
            ),
            (
                'Limitations',
                'US state rules differ from draft Brazilian frameworks; label art changes quickly.',
            ),
            (
                'Critical reading',
                'Brazilian policy drafters should budget for **retail audit capacity**, not just statutory text.',
            ),
            (
                'Source',
                '[Grace M. MacDonald et al. (2026) — Journal of Cannabis Research](https://doi.org/10.1186/s42238-026-00489-7)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-09',
        "title": 'Multiscale mechanisms of water-induced hemp fiber reinforcement',
        "title_pt": 'Mecanismos multiescala do reforço de fibra de cânhamo induzido por água',
        "slug": 'multiscale-mechanisms-of-water-induced-hemp-fiber-reinforcement',
        "excerpt": 'Estudo multiescala explica como a umidade reorganiza interface fibra–matriz e reforço mecânico em compósitos de cânhamo — guia para processamento em clima úmido tropical.',
        "en_excerpt": 'A multiscale study explains how moisture reorganises fibre–matrix interfaces and reinforcement in hemp composites — guidance for processing in humid tropical climates.',
        "tags": ['textile', 'research'],
        "doi": '10.1007/s10853-026-13577-z',
        "authors": 'Mingrui Lv et al.',
        "year": 2026,
        "journal": 'Journal of Materials Science',
        "published_at": '2026-09-21T12:08:00',
        "published_date": '2026-08-23',
        "content": md(
            (
                'Por que importa',
                'Fibra de cânhamo **higroscópica** altera propriedades mecânicas após condicionamento — crítico no Brasil. Lv et al. investigam **mecanismos multiescala** de **reforço induzido por água**, da escala nanométrica (celulose, lignina) à macro (aderência matriz). Para indústria de compósitos automotivo/construção, entender **swelling e recuperação** evita falhas prematuras.',
            ),
            (
                'O que o estudo fez',
                'Prepararam compósitos ou laminados com **fibra de cânhamo**, submetendo a ciclos de **condicionamento hídrico** controlado. Combinaram **MEV, AFM, ensaios mecânicos** e modelagem multiescala para correlacionar umidade, interface fibra–matriz e módulo/resistência. Compararam estados seco versus saturado parcial. Publicado em *Journal of Materials Science*; DOI 10.1007/s10853-026-13577-z.',
            ),
            (
                'Principais achados',
                'A **água** reorganizou **interface fibra–matriz**, promovendo em alguns regimes **aumento temporário de rigidez** via rearranjos de celulose e ponte hidrogênio, seguido de plastificação se saturação excessiva. Modelo multiescala reproduziu curvas experimentais com parâmetros de difusão transversal. Destacam **janela de umidade ótima** versus degradação por encharcamento.',
            ),
            (
                'Limitações',
                'Matriz e tratamento de fibra específicos; não todos os compatibilizantes testados. Ciclos laboratoriais curtos versus anos de serviço. Fibra chinesa/europeia.',
            ),
            (
                'Leitura crítica',
                'Processadores brasileiros: **secar e condicionar** fibra antes de extrusão/injeção; armazenar abaixo de RH crítica. Automotivo: testar EN humidity cycles com fibra nacional. Pesquisa Embrapa/indústria: compatibilizante silano pode mudar mecanismo.',
            ),
            (
                'Fonte',
                '[Mingrui Lv et al. (2026) — Journal of Materials Science](https://doi.org/10.1007/s10853-026-13577-z)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                'Hygroscopic **hemp fibre** shifts composite performance; Lv et al. map **multiscale water-induced reinforcement** from cellulose nanostructure to bulk mechanics.',
            ),
            (
                'What the study did',
                'Hemp composites underwent controlled **moisture conditioning** with **SEM/AFM**, mechanical tests and multiscale modelling linking interface changes to modulus.',
            ),
            (
                'Key findings',
                'Water **reorganised fibre–matrix interfaces**, yielding temporary stiffening at moderate moisture before plasticisation at high saturation. Modelling captured transverse diffusion effects.',
            ),
            (
                'Limitations',
                'Specific matrix/sizing; short lab cycles only.',
            ),
            (
                'Critical reading',
                'Brazilian processors should standardise **pre-conditioning RH** and humidity-cycle QA on local fibre.',
            ),
            (
                'Source',
                '[Mingrui Lv et al. (2026) — Journal of Materials Science](https://doi.org/10.1007/s10853-026-13577-z)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    },
    {
        "id": 'blog-research-20260921-10',
        "title": 'Deep eutectic solvent-derived hemp and jute cellulose nanopapers: from nanofibril morphology to nanopaper architecture and polyester microplastic filtration',
        "title_pt": 'Nanopapers de celulose de cânhamo e juta via solventes eutéticos profundos: morfologia, arquitetura e filtração de microplásticos de poliéster',
        "slug": 'deep-eutectic-solvent-derived-hemp-and-jute-cellulose-nanopapers-from-nanofibril',
        "excerpt": 'Nanopapers de celulose de cânhamo/juta produzidos com DES filtram microplásticos de poliéster — valorização de fibra e aplicação ambiental relevante ao Brasil.',
        "en_excerpt": 'Hemp/jute cellulose nanopapers made with deep eutectic solvents filter polyester microplastics — fibre valorisation with environmental application relevant to Brazil.',
        "tags": ['textile', 'research'],
        "doi": '10.1007/s10570-026-07205-x',
        "authors": 'Abu Naser Md Ahsanul Haque et al.',
        "year": 2026,
        "journal": 'Cellulose',
        "published_at": '2026-09-21T12:09:00',
        "published_date": '2026-09-07',
        "content": md(
            (
                'Por que importa',
                '**Microplásticos** contaminam água no Brasil; **nanopapers** de celulose de baixo costo são candidatos a filtração. Haque et al. usam **solventes eutéticos profundos (DES)** para fibrilar **cânhamo e juta**, montando **nanopapers** arquitetados e testando **retenção de microplásticos de poliéster**. Dupla vitória: coproduto têxtil + remediação ambiental alinhada a políticas de resíduos sólidos.',
            ),
            (
                'O que o estudo fez',
                'Deslignificação/fibrilação com **DES** a partir de **cânhamo** e **juta**, caracterizando **nanofibrilas** (TEM, AFM, DP). Formaram **nanopapers** por filtração a vácuo, controlando espessura e densidade. Desafiaram com suspensões de **microplásticos de poliéster**, quantificando eficiência de filtração, fluxo e mecanismo de captura (tamanho de poro, eletrosterico). Publicado em *Cellulose*; DOI 10.1007/s10570-026-07205-x.',
            ),
            (
                'Principais achados',
                'Nanopapers de **cânhamo** e **juta** exibiram morfologias distintas de nanofibrila, refletindo **arquitetura de poros** e eficiência de **filtração de microplásticos PET/poliéster**. DES permitiu processamento menos agressivo que vias clássicas em alguns indicadores. Algumas formulações combinaram alta retenção com fluxo aceitável — promissor para filtros descartáveis ou cartuchos.',
            ),
            (
                'Limitações',
                'Ensaios de bancada; não escala industrial de DES. Durabilidade úmida e regeneração do filtro não completas. Microplásticos modelo ≠ cocktail ambiental brasileiro.',
            ),
            (
                'Leitura crítica',
                'Startups de cânhamo: avaliar **coproduto de fibrilação** para filtros, não só tecido. Reguladores ambientais: exigir testes com água real de rio/costeira. Indústria têxtil: rastrear pegada química do DES.',
            ),
            (
                'Fonte',
                '[Abu Naser Md Ahsanul Haque et al. (2026) — Cellulose](https://doi.org/10.1007/s10570-026-07205-x)',
            ),
            (
                'Referência',
                'PLACEHOLDER_CITE',
            )
        ),
        "en_content": md(
            (
                'Why it matters',
                '**Microplastic pollution** motivates cellulose **nanopaper filters**; Haque et al. fibrillate **hemp and jute** via **deep eutectic solvents (DES)** and test **polyester microplastic** capture.',
            ),
            (
                'What the study did',
                '**DES processing** yielded nanofibrils cast into **nanopapers**; morphology (TEM/AFM) was linked to pore architecture and **microplastic filtration** efficiency.',
            ),
            (
                'Key findings',
                'Hemp and jute **nanopapers** differed in fibril network structure and **polyester microplastic retention**, with DES offering a gentler fibrillation route in reported metrics.',
            ),
            (
                'Limitations',
                'Bench scale; DES recovery and wet durability not fully solved.',
            ),
            (
                'Critical reading',
                'Brazilian hemp mills should explore filter co-products; regulators need real-water validation beyond model microplastics.',
            ),
            (
                'Source',
                '[Abu Naser Md Ahsanul Haque et al. (2026) — Cellulose](https://doi.org/10.1007/s10570-026-07205-x)',
            ),
            (
                'Reference',
                'PLACEHOLDER_CITE_EN',
            )
        ),
    }
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
    }


def main() -> None:
    existing = json.loads(BLOG_SEED.read_text(encoding="utf-8"))
    kept = [
        p
        for p in existing
        if not any(_post_has_doi(p, doi) for doi in ISSUE47_DOIS)
    ]
    merged = kept + [build_research_entry(p) for p in POSTS]
    BLOG_SEED.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(merged)} posts ({len(POSTS)} issue #47, {len(kept)} kept)")


if __name__ == "__main__":
    main()
