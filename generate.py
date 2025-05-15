# import os
# import json
# from dotenv import load_dotenv
# from openai import OpenAI

# # Load .env into environment
# load_dotenv()

# # Instantiate the OpenAI client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# SYSTEM_PROMPT = """
# You are a CBRE-branded presentation assistant. 
# Structure each slide with the following format:
# - Title: a clear, concise uppercase headline.
# - Content: 
#    • 3 paragraph at least for each slides, always start with a compelling intro in first slide, each paragraph bullet should contain at least 4-5 lines of text when needed, make the paragraph comprehensive and informative.
#    • A bulleted list (3–5 items) if sub-points are needed.

# The final slide must include a powerful call-to-action or takeaway.
# Given a request for N slides on X, produce EXACTLY N slides in JSON:
# {
#   "slides": [
#     {
#       "title": "Slide title",
#       "body": ["bullet1", "bullet2", …]
#     },
#     …
#   ]
# }
# Use professional, corporate-grade language.
# """

# def generate_slides(topic: str, n_slides: int):
#     user_msg = f"Generate {n_slides} slides on: {topic}"
#     resp = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user",   "content": user_msg}
#         ],
#         temperature=0.3,
#     )
#     data = json.loads(resp.choices[0].message.content)
#     if len(data.get("slides", [])) != n_slides:
#         raise ValueError(f"Expected {n_slides} slides, got {len(data.get('slides', []))}")
#     return data


import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# Load .env into environment
load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are a CBRE-branded presentation assistant. 
Structure each slide with the following format:
- Title: a clear, concise uppercase headline.
- Content: 
   • At least 3 paragraphs per slide when needed. Start with a compelling introduction for slide 1.
   • Each bullet paragraph should contain 4–5 lines of detailed, informative text.
   • Add a bulleted list (3–5 items) only if relevant.

The final slide must include a powerful call-to-action or takeaway.
Given a request for N slides on X, produce EXACTLY N slides in this format:
{
  "slides": [
    {
      "title": "SLIDE TITLE",
      "body": ["bullet1", "bullet2", …]
    },
    …
  ]
}
Use corporate, professional language. Output only valid JSON.
"""

def generate_slides(topic: str, n_slides: int):
    user_msg = f"Generate {n_slides} slides on: {topic}"

    # Retry logic: attempt up to 2 times if count mismatch
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_msg}
                ],
                temperature=0.3
            )
            data = json.loads(resp.choices[0].message.content)
            slides = data.get("slides", [])

            if len(slides) < n_slides:
                # Pad with placeholders
                for i in range(len(slides), n_slides):
                    slides.append({
                        "title": f"Extra Slide {i+1}",
                        "body": [f"Additional information on '{topic}' will go here."]
                    })

            return {"slides": slides[:n_slides]}

        except Exception as e:
            if attempt == 1:
                raise ValueError(f"Slide generation failed after 2 attempts: {e}")

    raise RuntimeError("Unexpected failure in slide generation.")
