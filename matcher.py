from difflib import SequenceMatcher

def match_job(summary, job_desc):
    ratio = SequenceMatcher(None, summary.lower(), job_desc.lower()).ratio()
    score = round(ratio * 100, 2)
    return {
        "match_score": score,
        "match_result": "Match" if score >= 50 else "No Match"
    }
