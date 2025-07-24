import os
import json
from openai import OpenAI

system_prompt = """
You are a smart data cleaner.

Given a noisy product review page, extract only the clean structured data per review:
1. Product Name
2. Rating (out of 5)
3. Review Text

Requirements:
- Remove all irrelevant content such as ads, HTML, links, non-text elements, and metadata.
- Ensure the output contains no emojis, special symbols, or formatting characters.
- Output clean, natural language in all fields.
- Remove all emojis and symbols like 👍🙂💯 from the review text and product names.
- Return the result as a valid JSON list, like:

[
  {
    "product_name": "...",
    "rating": 5,
    "review": "..."
  }
]
"""

def extract_reviews(text, client, model, temperature, max_tokens):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    content = response.choices[0].message.content
    # return content
    try:
        json_start = content.find("[")
        json_end = content.rfind("]") + 1
        json_str = content[json_start:json_end]
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print("JSON parse error:", e)
        print("Raw response:\n", content[:500])
        return []
