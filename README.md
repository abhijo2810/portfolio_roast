# `portfolio_roast`

`portfolio_roast` is a Python package that humorously roasts your trading strategy `.py` files using OpenAI GPT-4. It analyzes your code structure and delivers a sarcastic critique to keep you entertained while coding.

## Features

- Parses Python files to identify key structures like functions, loops, and constants.
- Generates a sarcastic roast based on your trading strategy code.
- Easy-to-use CLI tool: `portfolio-roast my_strategy.py`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/portfolio_roast.git
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

### Example Output

```plaintext
Analyzing your trading strategy...
Roast incoming:
"Wow, a `while True` loop? Bold move. I guess you really wanted to make sure your strategy never stops losing money. And those hardcoded constants? Truly the hallmark of a professional quant."
```

## How It Works

1. **File Parsing**: The `roast_strategy` function reads your Python file and uses the `ast` module to analyze its structure.
2. **Prompt Generation**: It creates a sarcastic prompt based on the code's structure.
3. **OpenAI API**: Sends the prompt to GPT-4 and retrieves the roast.
4. **CLI Tool**: Wraps everything in a command-line interface for easy use.

## Error Handling

- Ensures the file exists and is a valid Python file.
- Handles API errors gracefully and provides meaningful error messages.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This package is for entertainment purposes only. Don't take the roasts personally—your trading strategy is probably great!
