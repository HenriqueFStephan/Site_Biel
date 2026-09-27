"""Infer research_area for blog posts from agent tags and title/excerpt heuristics."""

from __future__ import annotations

import re

from app.models.schemas import ResearchArea

_CONSTRUCTION = re.compile(
    r"hempcrete|hemp[- ]lime|building engineering|bio-?composite|hemp board|"
    r"earth[–-]hemp|machining stability in hemp|thermal and acoustic properties|"
    r"low-carbon binders|hydraulic lime|effect of technological variables on thermal",
    re.I,
)
_CLINICAL = re.compile(
    r"patient|clinical|trial|rct|symptom|pain|cancer|arthritis|driving|edible|"
    r"pharmacokinetic|postsurgical|sleep|cross-over|dose-dependent|medicinal cannabis|"
    r"cardiovascular|prenatal|executive function",
    re.I,
)


def infer_research_area(*, tags: list[str], title: str, excerpt: str = "") -> ResearchArea | None:
    tag_set = set(tags)
    blob = f"{title} {excerpt}"

    if "policy" in tag_set:
        return ResearchArea.REGULATORIO
    if "medical" in tag_set:
        if "cultivation" in tag_set:
            return ResearchArea.MEDICINAL if _CLINICAL.search(blob) else ResearchArea.AGRONOMIA
        return ResearchArea.MEDICINAL
    if "cultivation" in tag_set:
        return ResearchArea.AGRONOMIA
    if "textile" in tag_set:
        return ResearchArea.CONSTRUCAO if _CONSTRUCTION.search(blob) else ResearchArea.TEXTIL
    return None
