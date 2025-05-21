import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from roast import roast_strategy
from analyzer import summarize_code

import subprocess
import os

print("🔎 Code Summary:", summarize_code("examples/sample_strategy.py"))

# def test_cli_py_runs():
#     example_path = os.path.join("examples", "sample_strategy.py")
#     result = subprocess.run(["python", "cli.py", example_path], capture_output=True, text=True)
#     assert "roast" in result.stdout.lower() or "skipped" in result.stdout.lower()

# def test_cli_csv_roast():
#     path = os.path.join("examples", "sample_trades.csv")
#     result = subprocess.run(["python", "cli.py", path], capture_output=True, text=True)
#     assert "roast" in result.stdout.lower() or "skipped" in result.stdout.lower()

if __name__ == "__main__":
    result = roast_strategy("examples/sample_strategy.py")
    print("\n📣 GPT Roast:\n")
    print(result)
    



