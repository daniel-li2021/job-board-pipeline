"""Deterministic evidence warnings, separate from technical fit scores."""
import re

EMPLOYER_UNKNOWN = "Employer unverified"
JD_UNVERIFIED = "Suggested/proposed JD; verify original"
COHORT_UNVERIFIED = "Graduation eligibility unverified"

# These are explicit disclaimers, not a classifier for generic writing or fraud.
PLACEHOLDER_JD_RE = re.compile(
    r"\bthis suggested job description\b|"
    r"\bis listed as the (?:company|employer) for this (?:proposed )?[^.]{0,100}\bposition\b",
    re.I,
)
COHORT_TITLE_RE = re.compile(
    r"\b2027\b.*\b(?:graduate|graduating|new grad)\b|"
    r"\b(?:graduate|graduating|new grad)\b.*\b2027\b", re.I,
)


def evidence_warnings(job):
    """Derive current warnings; retain JD findings when reading a compact store."""
    if job.get("source") not in {"indeed", "linkedin", "glassdoor"}:
        return []
    warnings = []
    if not str(job.get("company") or "").strip():
        warnings.append(EMPLOYER_UNKNOWN)
    description = str(job.get("description") or "").strip()
    if PLACEHOLDER_JD_RE.search(description) or (
        not description and job.get("description_available")
        and JD_UNVERIFIED in (job.get("evidence_warnings") or [])
    ):
        warnings.append(JD_UNVERIFIED)
    if (len(description) < 200 and not job.get("description_available")
            and COHORT_TITLE_RE.search(str(job.get("title") or ""))):
        warnings.append(COHORT_UNVERIFIED)
    return warnings
