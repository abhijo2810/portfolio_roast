import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from roast import roast_strategy

if __name__ == "__main__":
    result = roast_strategy("examples/sample_strategy.py")
    print("\n📣 GPT Roast:\n")
    print(result)
