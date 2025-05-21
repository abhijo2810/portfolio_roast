# `portfolio_roast`

`portfolio_roast` is a GPT-powered command-line tool that delivers sarcastic, intelligent critiques of your trading strategy code or trading performance. It analyzes your code structure and delivers a sarcastic critique to keep you entertained while coding. Whether you feed it a Python strategy file or a CSV of your trade results, it will respond like a brutally honest trading mentor who's had enough of RSI crossovers and emotional exits.

## 🚀 Features

- 📂 Supports both `.py` strategy code and `.csv` trade logs
- 🤖 Uses OpenAI's GPT to generate entertaining and insightful feedback
- 🧠 Parses your code to summarize structure (functions, loops, constants)
- 📊 Computes basic trade performance metrics (win rate, profit factor, drawdown)
- ✅ Lightweight CLI for quick and repeatable use

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/abhijo2810/portfolio_roast.git
    cd portfolio_roast
    ```

2. Install the package:
    ```bash
    pip install .
    ```

3. Set your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

### CLI

Run the following command to roast your trading strategy file:
```bash
portfolio-roast my_strategy.py
```

### Token Usage

Each user is limited to a maximum of 5 responses. This ensures fair usage of the tool. The package does not display token usage details for privacy reasons, but keep this limit in mind while using the tool.

### Example Output

```plaintext
Analyzing your trading strategy...
Roast incoming:
"Wow, a `while True` loop? Bold move. I guess you really wanted to make sure your strategy never stops losing money. And those hardcoded constants? Truly the hallmark of a professional quant."
```


## 🔧 How It Works

1. 🧠 **Code Summarizer**: Uses Python’s ast module to parse trading strategy structure.
2. 📈 **Metrics Engine**: Analyzes trade data for key performance indicators.
3. 🧰 **Prompt Builder**: Crafts a GPT prompt based on your code or results.
4. 🗣️ **Roast Engine**: Queries GPT-3.5 for an honest, sarcastic critique.
5. 💻 **CLI Tool**: Combines everything into a clean command-line interface.

## Testing

To run tests for the package, use the following command:
```bash
python test_roast.py
```
This will simulate roast runs on both .py and .csv examples. This ensures that all functionalities are working as expected.

## Contributing

At this time, contributions are not being accepted as this is a personal project. Thank you for your understanding.

## 💬 Feedback

Have thoughts, roasts of the roast, or bugs to report?

👉 [Open an Issue](https://github.com/abhijo2810/portfolio_roast/issues)  
👉 Or join the Discussion tab and say hi!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is meant for educational and entertainment purposes only.
The feedback is AI-generated and intentionally sarcastic please don’t take it personally — your trading strategy is probably great!
Use your own judgment before using any roasted strategy in real markets.
