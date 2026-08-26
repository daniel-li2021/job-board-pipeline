"""Uber official careers adapter.

jobs.uber.com HTML does not paginate. The careers UI is Oracle Cloud HCM:

    https://iaziqy.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/UberCareers

List: GET ``/hcmRestApi/resources/latest/recruitingCEJobRequisitions``
with ``finder=findReqs;siteNumber=CX_1,limit,offset,keyword``.
``offset = (page - 1) * pagesize``. Paginate until TotalJobsCount is
exhausted — do not stop at pages 1–7.

The HCM finder does not honor a reliable United States country filter, so
rows are collected then passed through the shared conservative US helper.
Canonical apply URL stays ``https://jobs.uber.com/en/jobs/{id}/``.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import requests

from .oracle_hcm import scrape_oracle_hcm

UBER_HOST = "https://iaziqy.fa.ocs.oraclecloud.com"
UBER_SITE = "CX_1"
UBER_PUBLIC = "https://jobs.uber.com/en/jobs"


def scrape_uber(
    session: requests.Session,
    *,
    max_pages: int = 50,
    queries: Optional[List[str]] = None,
    fetch_details: bool = True,
) -> Dict[str, Any]:
    result = scrape_oracle_hcm(
        session,
        company="Uber",
        host=UBER_HOST,
        site_number=UBER_SITE,
        public_job_base=UBER_PUBLIC,
        max_pages=max_pages,
        queries=queries,
        fetch_details=fetch_details,
    )
    result["method"] = (
        "HTTP GET Oracle HCM recruitingCEJobRequisitions on iaziqy.fa.ocs.oraclecloud.com "
        "(offset pagination) + recruitingCEJobRequisitionDetails"
    )
    result["search_url"] = "https://jobs.uber.com/en/jobs/?search=software%20engineer&page=1&pagesize=10"
    result["pagination"] = (
        "HCM finder offset=(page-1)*limit ; limit=20; stop on empty/repeat or TotalJobsCount "
        "(do not stop at pages 1–7)"
    )
    return result
