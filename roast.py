import os
from dotenv import load_dotenv
import openai
from analyzer import summarize_code
from prompts import build_prompt

load_dotenv()  # Load variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def roast_strategy(file_path: str) -> str:
    try:
        with open(file_path, 'r') as f:
            code = f.read()
    except Exception as e:
        return f"Error reading file: {e}"

    summary = summarize_code(file_path)
    prompt = build_prompt(code, summary)

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=500
        )
        roast = response.choices[0].message.content

        return roast
    except Exception as e:
        return f"OpenAI API error: {e}"

