from scraper import fetch_page
from extractor import extract_jobs
from classifier import is_relevant
from db import get_db

CAREER_URLS = [
    "https://careers.google.com/jobs/",
    "https://razorpay.com/jobs/"
]

def run_agent():
    conn = get_db()
    c = conn.cursor()

    for url in CAREER_URLS:
        company = url.split("//")[-1].split(".")[0].capitalize()
        html = fetch_page(url)
        jobs = extract_jobs(html, company)

        for j in jobs:
            if j.get("job_title") and is_relevant(j["job_title"]):
                c.execute(
                    "INSERT INTO jobs (company, job_title, location, job_link) VALUES (?,?,?,?)",
                    (company, j["job_title"], j.get("location"), j.get("job_link"))
                )

    conn.commit()
    conn.close()
