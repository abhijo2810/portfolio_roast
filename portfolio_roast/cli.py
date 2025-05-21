import argparse
from portfolio_roast.roast import roast_strategy, roast_csv
from portfolio_roast.usage_tracker import increment_and_check_limit, MAX_USES

def main():
    allowed, count = increment_and_check_limit()
    if not allowed:
        print(f"❌ You've reached the free usage limit of {MAX_USES} roasts.")
        print("💬 Contact the developer if you'd like extended access.")
        return

    parser = argparse.ArgumentParser(description="Roast a trading strategy (.py) or trade log (.csv)")
    parser.add_argument("file_path", help="Path to the .py or .csv file to roast")
    args = parser.parse_args()

    file = args.file_path
    print(f"🔥 Roasting: {file}")

    if file.endswith(".csv"):
        roast = roast_csv(file)
    elif file.endswith(".py"):
        roast = roast_strategy(file)
    else:
        roast = "Unsupported file type."

    print(roast)
    print(f"\n🧮 Roasts used: {count}/{MAX_USES}")


if __name__ == "__main__":
    main()