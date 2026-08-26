"""Big Tech Official Careers discovery adapters.

Discovery only. Each adapter returns unified job dicts from ``sources.schema.make_job``.
Matching / hard-filter / LLM scoring / Tier A/B ranking stay in ``board_pipeline.py``.
"""

from .amazon import scrape_amazon
from .apple import scrape_apple
from .ashby import scrape_ashby
from .avature import scrape_avature
from .google import scrape_google
from .greenhouse import scrape_greenhouse
from .microsoft import scrape_microsoft
from .oracle_hcm import scrape_oracle_hcm
from .registry import load_companies, scrape_company, scrape_enabled
from .sap import scrape_sap
from .smartrecruiters import scrape_smartrecruiters
from .uber import scrape_uber
from .workday import scrape_workday

__all__ = [
    "load_companies",
    "scrape_amazon",
    "scrape_apple",
    "scrape_ashby",
    "scrape_avature",
    "scrape_company",
    "scrape_enabled",
    "scrape_google",
    "scrape_greenhouse",
    "scrape_microsoft",
    "scrape_oracle_hcm",
    "scrape_sap",
    "scrape_smartrecruiters",
    "scrape_uber",
    "scrape_workday",
]
