import unittest

from sources.careers.disney import scrape_disney
from sources.careers.linkedin_company import scrape_linkedin_company
from sources.careers.meta import scrape_meta
from sources.careers.tiktok import scrape_tiktok
from sources.careers.walmart import scrape_walmart


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
