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

def build_prompt(code, summary):
    return f"""You're a sarcastic trading mentor. Here’s the code and a summary:

CODE:
{code}

SUMMARY:
{summary}

Roast it with wit, sarcasm, and brutal honesty — but make it funny and educational.
"""

def build_csv_prompt(metrics):
    return f"""You're a savage trading coach reviewing strategy performance.

Here are the stats:
- Total trades: {metrics['total_trades']}
- Win rate: {metrics['win_rate'] * 100}%
- Profit factor: {metrics['profit_factor']}
- Avg R/R: {metrics['avg_risk_reward']}
- Max drawdown: {metrics['max_drawdown']}

Roast these numbers like you're ripping apart someone's trading dreams — with humor, realism, and snark.
"""
