import openai
from dotenv import load_dotenv
import os

load_dotenv()

response = openai.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[{"role": "user", "content": "Roast this trading strategy: Buy high, sell low."}],
    temperature=0.7,
)

print(response.choices[0].message.content)

# Show token usage
print("\nUSAGE:")
print(response.usage)
print("Prompt tokens:", response.usage.prompt_tokens)
print("Completion tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)

