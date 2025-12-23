import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_jobs(html, company):
    prompt = f"""
    Extract job listings from HTML.
    Return JSON array with job_title, location, job_link.

    HTML:
    {html[:12000]}
    """

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    try:
        jobs = json.loads(r.choices[0].message.content)
        for j in jobs:
            j["company"] = company
        return jobs
    except:
        return []
