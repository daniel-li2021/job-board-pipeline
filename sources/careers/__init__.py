"""Big Tech Official Careers discovery adapters.

Discovery only. Each adapter returns unified job dicts from ``sources.schema.make_job``.
Matching / hard-filter / LLM scoring / Tier A/B ranking stay in ``board_pipeline.py``.
"""

from .amazon import scrape_amazon
from .apple import scrape_apple
from .ashby import scrape_ashby
from .avature import scrape_avature
from .disney import scrape_disney
from .google import scrape_google
from .greenhouse import scrape_greenhouse
from .lever import scrape_lever
from .linkedin_company import scrape_linkedin_company
from .meta import scrape_meta
from .microsoft import scrape_microsoft, scrape_pcsx
from .oracle_hcm import scrape_oracle_hcm
from .registry import load_companies, scrape_company, scrape_enabled
from .sap import scrape_sap
from .smartrecruiters import scrape_smartrecruiters
from .tiktok import scrape_tiktok
from .uber import scrape_uber
from .workday import scrape_workday
from .walmart import scrape_walmart

__all__ = [
    "load_companies",
    "scrape_amazon",
    "scrape_apple",
    "scrape_ashby",
    "scrape_avature",
    "scrape_disney",
    "scrape_company",
    "scrape_enabled",
    "scrape_google",
    "scrape_greenhouse",
    "scrape_lever",
    "scrape_linkedin_company",
    "scrape_meta",
    "scrape_microsoft",
    "scrape_pcsx",
    "scrape_oracle_hcm",
    "scrape_sap",
    "scrape_smartrecruiters",
    "scrape_tiktok",
    "scrape_uber",
    "scrape_workday",
    "scrape_walmart",
]
