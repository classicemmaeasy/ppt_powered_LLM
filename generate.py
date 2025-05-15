# import os, json
# import openai
# import numpy as np
# from numpy.linalg import norm

# openai.api_key = os.getenv("OPENAI_API_KEY")

# SYSTEM_PROMPT = """
# You are a CBRE-branded presentation assistant. 
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
#     resp = openai.ChatCompletion.create(
#         model="gpt-4",
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



# generate.py
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load .env into environment
load_dotenv()

# Instantiate the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a CBRE-branded presentation assistant. 
Structure each slide with the following format:
- Title: a clear, concise uppercase headline.
- Content: 
   • 3 paragraph at least for each slides, always start with a compelling intro in first slide, each paragraph bullet should contain at least 4-5 lines of text when needed, make the paragraph comprehensive and informative.
   • A bulleted list (3–5 items) if sub-points are needed.

The final slide must include a powerful call-to-action or takeaway.
Given a request for N slides on X, produce EXACTLY N slides in JSON:
{
  "slides": [
    {
      "title": "Slide title",
      "body": ["bullet1", "bullet2", …]
    },
    …
  ]
}
Use professional, corporate-grade language.
"""

def generate_slides(topic: str, n_slides: int):
    user_msg = f"Generate {n_slides} slides on: {topic}"
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_msg}
        ],
        temperature=0.3,
    )
    data = json.loads(resp.choices[0].message.content)
    if len(data.get("slides", [])) != n_slides:
        raise ValueError(f"Expected {n_slides} slides, got {len(data.get('slides', []))}")
    return data
