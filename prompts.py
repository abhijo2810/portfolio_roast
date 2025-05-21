def build_prompt(code: str, summary: str) -> str:
    return f"""
You are a sarcastic but insightful trading mentor.

This is a user's strategy summary:
{summary}

And here's their actual code:
{code}

Please roast this strategy like you're a trading wizard who’s seen too many dumb scripts.
Be sharp, witty, and brutally helpful. 
Mention anything that's risky, weird, redundant, or flat-out wrong.

Also give one or two useful suggestions. 
Keep it under 300 words. Add a final funny line.
"""
