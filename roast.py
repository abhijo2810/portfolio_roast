import os
from dotenv import load_dotenv
import openai
from analyzer import summarize_code
from prompts import build_prompt, build_csv_prompt
from metrics import analyze_trades

load_dotenv()  # Load variables from .env

def display_usage_info(usage):
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    # Pricing for gpt-3.5-turbo-0125 (as of 2024)
    prompt_cost = prompt_tokens * 0.0005 / 1000
    completion_cost = completion_tokens * 0.0015 / 1000
    total_cost = prompt_cost + completion_cost

    print("\n📊 Token Usage & Cost:")
    print(f"- Prompt tokens:     {prompt_tokens}")
    print(f"- Completion tokens: {completion_tokens}")
    print(f"- Total tokens:      {total_tokens}")
    print(f"- Estimated cost:    ${total_cost:.6f} USD")

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
        display_usage_info(response.usage)
        return roast
    except Exception as e:
        return f"OpenAI API error: {e}"

def roast_csv(csv_path):
    metrics = analyze_trades(csv_path)
    prompt = build_csv_prompt(metrics)

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.8,
        )
        roast = response.choices[0].message.content
        print(roast)
        display_usage_info(response.usage)

    except Exception as e:
        roast = f"[ERROR] OpenAI API call failed: {e}"