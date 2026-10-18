# Batch 1 offline evidence fixtures

Source revision: `16b8bcdbbf3f9fd1b4bac13b968701313e3fc0f3`.

- `meta_detail.html`: only the public JobPosting fields needed for the parser, extracted from the investigation's saved October 17, 2026 response for `https://www.metacareers.com/profile/job_details/1404071541713403`. The public posting title, numeric URL ID, differing schema identifier, responsibilities, and qualifications are retained. All page scripts, cookies, tracking, and unrelated markup are removed.
- `twosigma_detail.html`: the three `article.article--details` blocks from the saved public response for `https://careers.twosigma.com/careers/JobDetail/New-York-City-United-States-Quantitative-Software-Engineer-Generative-AI/13079`. It preserves the two 80-character metadata blocks before the 3,959-character JD. Other page scripts/navigation/tracking are removed. Extraction depends only on the original article blocks.
- `early_career_saved.json`: four employer job descriptions and original record IDs from the pinned `output/recovery/syncareer.json.gz`: CoStar SWE I, two NVIDIA new-college-grad records, and a WEX graduate internship. Candidate/resume/matching/application data is excluded. These test admission to the role prefilter, not availability, final suitability, or final ranking.

These are offline parser/filter fixtures. No current availability or live recovery rate is implied.
