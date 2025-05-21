import argparse
from roast import roast_strategy, roast_csv

def main():
    parser = argparse.ArgumentParser(description="Roast a trading strategy (code or CSV).")
    parser.add_argument("file_path", help="Path to the .py or .csv file to roast.")
    args = parser.parse_args()

    if args.file_path.endswith(".csv"):
        roast_csv(args.file_path)
    elif args.file_path.endswith(".py"):
        roast_strategy(args.file_path)
    else:
        print("Unsupported file type. Please provide a .py or .csv file.")

if __name__ == "__main__":
    main()