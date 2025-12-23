import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def is_relevant(title):
    prompt = f"""
    Is this Product Management or Business/Data Analytics role?
    Title: {title}
    Answer YES or NO.
    """

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return "YES" in r.choices[0].message.content
