import json
import unittest

from sources.careers.avature import scrape_avature
from sources.careers.disney import scrape_disney
from sources.careers.eightfold_html import scrape_eightfold_html
from sources.careers.happydance import scrape_happydance
from sources.careers.jibe import scrape_jibe
from sources.careers.linkedin_company import scrape_linkedin_company
from sources.careers.mathworks import scrape_mathworks
from sources.careers.meta import scrape_meta
from sources.careers.radancy import scrape_radancy
from sources.careers.tiktok import scrape_bytedance, scrape_tiktok
from sources.careers.walmart import scrape_walmart
from sources.careers.workday import _us_facet


class Response:
    def __init__(self, *, payload=None, text="", status=200):
        self._payload = payload
        self.text = text
        self.status_code = status

    def json(self):
        return self._payload


class Session:
    def __init__(self, gets=None, posts=None):
        self.gets = list(gets or [])
        self.posts = list(posts or [])
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append(("GET", url, kwargs))
        return self.gets.pop(0)

    def post(self, url, **kwargs):
        self.calls.append(("POST", url, kwargs))
        return self.posts.pop(0)


class OfficialAdapterTests(unittest.TestCase):
    def test_walmart_uses_required_hybrid_payload(self):
        session = Session(posts=[Response(payload={
            "jobs": [{"id": "R-1-External", "text": "Build software", "metadata": {
                "jobId": "R-1", "jobPostingTitle": "Software Engineer",
                "primaryLocationCity": "Bentonville", "primaryLocationState": "AR",
                "primaryLocationCountry": "US", "jobPostingStartDate": 1787788800000,
            }}],
            "totalJobs": 1,
        })])
        result = scrape_walmart(session, max_pages=1, queries=["software"])
        self.assertEqual("R-1", result["jobs"][0]["job_id"])
        call = session.calls[0][2]
        self.assertEqual({"query": "software", "basicSearch": False, "filter": "", "locale": "en_US"}, call["json"])
        self.assertEqual(0, call["params"]["page"])

    def test_tiktok_keeps_lifeattiktok_canonical_url(self):
        session = Session(posts=[Response(payload={"code": 0, "data": {
            "count": 1,
            "job_post_list": [{
                "id": "123", "title": "Machine Learning Engineer", "description": "Build AI",
                "requirement": "Python", "city_info": {"en_name": "Seattle", "parent": {
                    "en_name": "Washington", "parent": {"en_name": "United States of America"}
                }},
            }],
        }})])
        result = scrape_tiktok(session, max_pages=1, queries=["machine learning engineer"])
        self.assertEqual("https://lifeattiktok.com/search/123", result["jobs"][0]["official_url"])
        self.assertTrue(session.calls[0][2]["json"]["location_code_list"])

    def test_bytedance_uses_shared_supplier_api_with_required_environment_header(self):
        session = Session(posts=[Response(payload={"code": 0, "data": {
            "count": 1,
            "job_post_list": [{
                "id": "456", "title": "Backend Software Engineer", "description": "Build APIs",
                "requirement": "Python", "city_info": {"en_name": "San Jose", "parent": {
                    "en_name": "California", "parent": {"en_name": "United States of America"}
                }},
            }],
        }})])
        result = scrape_bytedance(session, max_pages=1, queries=["software engineer"])
        self.assertEqual("https://joinbytedance.com/search/456", result["jobs"][0]["official_url"])
        call = session.calls[0][2]
        self.assertEqual("boe_epam_api", call["headers"]["x-tt-env"])
        self.assertEqual([], call["json"]["recruitment_id_list"])

    def test_workday_collects_modern_us_location_facets(self):
        facets = [{"facetParameter": "locations", "values": [
            {"id": "remote-us", "descriptor": "Remote-USA"},
            {"id": "remote-de", "descriptor": "Remote-Germany"},
            {"id": "austin", "descriptor": "Austin, Texas, United States of America"},
        ]}]
        self.assertEqual({"locations": ["remote-us", "austin"]}, _us_facet(facets))

    def test_radancy_parses_server_rendered_us_table(self):
        html = """<table data-controller="jobs--table-results"><tbody>
          <tr data-job-url="https://careers.example/jobs/software-engineer">
            <td class="job-search-results-title"><a>Software Engineer</a></td>
            <td class="job-search-results-requisition-identifiers">JR-1</td>
            <td class="job-search-results-location"><ul><li>Dallas, Texas, United States</li></ul></td>
          </tr></tbody></table>"""
        session = Session(gets=[Response(text=html)])
        result = scrape_radancy(
            session, company="Example", search_url="https://careers.example/jobs/search",
            max_pages=1, queries=["software engineer"], fetch_details=False,
        )
        self.assertEqual(["JR-1"], [job["job_id"] for job in result["jobs"]])
        self.assertEqual("US", session.calls[0][2]["params"]["country_codes[]"])

    def test_radancy_supports_talentbrew_query_and_pagination_parameters(self):
        html = """<ul id="search-results-list"><li class="search-results-list__list-item">
          <a class="sr-job-link" href="/job/a/software-engineer/1/42"><h2>Software Engineer</h2></a>
          <span class="job-location">San Jose, California, United States</span>
          <span class="jobId">Job ID: 42</span></li></ul>"""
        session = Session(gets=[Response(text=html)])
        result = scrape_radancy(
            session, company="Example", search_url="https://careers.example/search-jobs",
            max_pages=1, queries=["software"], fetch_details=False,
            query_param="k", page_param="p", country_param=None, page_size=15,
        )
        self.assertEqual(["42"], [job["job_id"] for job in result["jobs"]])
        self.assertEqual({"k": "software", "p": 1}, session.calls[0][2]["params"])

    def test_eightfold_html_reads_embedded_public_positions(self):
        payload = {"positions": [{
            "id": 5, "ats_job_id": "JR5", "posting_name": "Software Engineer",
            "locations": ["Los Gatos, California, United States of America"],
            "t_create": 1787702400,
            "canonicalPositionUrl": "https://jobs.example/careers/job/5",
        }]}
        html = f'<code id="smartApplyData">{json.dumps(payload)}</code>'
        result = scrape_eightfold_html(
            Session(gets=[Response(text=html)]), company="Example",
            portal="https://jobs.example/careers", domain="example.com", queries=["software"],
        )
        self.assertEqual(["JR5"], [job["job_id"] for job in result["jobs"]])

    def test_jibe_reads_complete_public_job_rows(self):
        payload = {"jobs": [{"data": {
            "req_id": "A1", "title": "AI Engineer", "full_location": "Austin, Texas",
            "canonical_url": "https://careers.example/jobs/A1", "description": "Build AI",
            "create_date": "2026-08-30T00:00:00+0000",
        }}], "totalCount": 1, "filter": {"displayLimit": 10}}
        result = scrape_jibe(
            Session(gets=[Response(payload=payload)]), company="Example",
            api_url="https://careers.example/api/jobs", max_pages=1, queries=["AI engineer"],
        )
        self.assertEqual(["A1"], [job["job_id"] for job in result["jobs"]])

    def test_mathworks_parses_server_rendered_search(self):
        html = """<table><tr><td><input class="job_posting_checkbox" value="37333"></td>
          <td class="search_result_desc"><div class="search_title"><a href="/company/jobs/opportunities/37333-test">Software Engineer</a></div>
          <span class="add_font_color_green">US-MA-Natick</span></td></tr></table>"""
        result = scrape_mathworks(
            Session(gets=[Response(text=html)]), max_pages=1,
            queries=["software"], fetch_details=False,
        )
        self.assertEqual(["37333"], [job["job_id"] for job in result["jobs"]])

    def test_happydance_reads_paginated_public_api(self):
        payload = {"jobs": [{
            "Id": "r-1", "OriginalId": "R-1", "Title": "Software Engineer",
            "Locations": [{"Identifier": "Austin, Texas"}],
            "Urls": [{"Url": "/jobs/r-1/software-engineer/", "IsDefault": True}],
        }], "totalPages": 1}
        result = scrape_happydance(
            Session(gets=[Response(payload=payload)]), company="Example",
            base_url="https://careers.example", max_pages=1,
            queries=["software"], fetch_details=False,
        )
        self.assertEqual(["R-1"], [job["job_id"] for job in result["jobs"]])

    def test_avature_supports_alternate_search_parameter(self):
        html = """<article><a href="/careers/JobDetail/New-York-United-States-Software-Engineer/42">
          Software Engineer</a><span class="location">United States - NY New York</span></article>"""
        session = Session(gets=[Response(text=html)])
        result = scrape_avature(
            session, company="Example", search_url="https://careers.example/careers/OpenRoles",
            max_pages=1, queries=["software"], fetch_details=False,
            query_param="search", page_size=10, base_url="https://careers.example",
        )
        self.assertEqual(["42"], [job["job_id"] for job in result["jobs"]])
        self.assertEqual("software", session.calls[0][2]["params"]["search"])

    def test_linkedin_guest_search_only_accepts_linkedin_company(self):
        html = """
        <div class="job-search-card" data-entity-urn="urn:li:jobPosting:42">
          <a class="base-card__full-link" href="https://www.linkedin.com/jobs/view/example-42?tracking=x"></a>
          <h3 class="base-search-card__title">AI Engineer</h3>
          <h4 class="base-search-card__subtitle">LinkedIn</h4>
          <span class="job-search-card__location">Sunnyvale, CA</span><time datetime="2026-08-30"></time>
        </div>
        <div class="job-search-card" data-entity-urn="urn:li:jobPosting:99">
          <a class="base-card__full-link" href="https://example.test/99"></a>
          <h3 class="base-search-card__title">Wrong company</h3>
          <h4 class="base-search-card__subtitle">Other</h4>
        </div>"""
        result = scrape_linkedin_company(Session(gets=[Response(text=html)]), max_pages=1, queries=["ai engineer"])
        self.assertEqual(["42"], [job["job_id"] for job in result["jobs"]])
        self.assertEqual("https://www.linkedin.com/jobs/view/example-42", result["jobs"][0]["official_url"])

    def test_meta_discovers_lsd_and_doc_id(self):
        portal = '<script src="https://static.example/meta.js"></script>"LSD",[],{"token":"dynamic-token"}'
        bundle = 'CareersJobSearchResultsV2DataQuery_candidate_portalRelayOperation",[],(function(){a.exports="987654321"})'
        graph = {"data": {"job_search_with_featured_jobs_v2": {"all_jobs": [{
            "id": "88", "title": "Data Scientist", "locations": ["Menlo Park, CA"]
        }]}}}
        session = Session(gets=[Response(text=portal), Response(text=bundle)], posts=[Response(payload=graph)])
        result = scrape_meta(session, max_pages=1, queries=["data scientist"])
        self.assertEqual("88", result["jobs"][0]["job_id"])
        post = session.calls[-1][2]
        self.assertEqual("dynamic-token", post["data"]["lsd"])
        self.assertEqual("987654321", post["data"]["doc_id"])

    def test_disney_parses_server_rendered_search(self):
        html = """<ul id="search-results-jobs"><li><a data-job-id="1" data-job-secondary-id="D1"
          href="/en/job/test"><h2>Associate Software Engineer</h2>
          <span class="job-location">Orlando, Florida</span><span class="job-date-posted">Aug. 30, 2026</span>
          </a></li></ul><nav id="pagination-bottom"></nav>"""
        result = scrape_disney(Session(gets=[Response(text=html)]), max_pages=1, queries=["software engineer"])
        self.assertEqual("D1", result["jobs"][0]["job_id"])
        self.assertEqual("https://www.disneycareers.com/en/job/test", result["jobs"][0]["official_url"])


if __name__ == "__main__":
    unittest.main()
