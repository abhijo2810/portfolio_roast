from setuptools import setup, find_packages

setup(
    name="portfolio_roast",
    version="0.1.0",
    description="GPT-powered trading strategy and performance roaster",
    author="Ajit Johori",
    packages=find_packages(),
    install_requires=[
        "openai",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "portfolio-roast=portfolio_roast.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
