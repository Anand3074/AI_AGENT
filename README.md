AI_AGENT 🧠⚡

This repository contains an AI Agent project built with Python along with a Calculator module (with both CLI and Tkinter UI support).

📂 Project Structure
AI_AGENT/
│── call_function.py       # Function caller module for AI agent
│── config.py              # Configurations and constants
│── functions/             # Utility functions
│── main.py                # Entry point for AI Agent
│── tests.py               # Unit tests
│── pyproject.toml         # Project metadata
│── uv.lock                # Lock file for dependencies
│── README.md              # Documentation
│
└── calculator/            # Calculator module
    │── calculator.py      # CLI calculator
    │── calculator_ui.py   # Tkinter UI calculator
    │── main.py            # Entry point for calculator
    │── tests.py           # Calculator tests
    │── README.md          # Sub-project README
    │── Bill.txt           # Sample data
    │── lorem.txt          # Sample text file
    │── text/              # Text assets
    │── text.txt
    │── pkg/               # Supporting package files

🚀 Getting Started
1. Clone the repository
git clone https://github.com/Anand3074/AI_AGENT.git
cd AI_AGENT

2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Linux / macOS
.venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt


(If requirements.txt isn’t available, install manually as needed: tkinter, etc.)

🧑‍💻 Running the AI Agent

Run the main agent:

python main.py


This uses call_function.py, functions/, and config.py to process tasks dynamically.

🖩 Running the Calculator
CLI Calculator
cd calculator
python calculator.py "2 + 3 * (4 - 1)"

Tkinter UI Calculator
cd calculator
python calculator_ui.py


You’ll get a simple GUI where you can type expressions and see results.

🧪 Running Tests
pytest


Tests are available for both the AI Agent and the Calculator.

📖 Features
AI Agent

Function calling system (call_function.py)

Modular design (functions/ directory)

Configurable setup (config.py)

Calculator

CLI calculator with expression evaluation

Tkinter-based GUI calculator

Sample data files for testing

📌 Future Improvements

Add more advanced AI agent functions

Expand calculator to support scientific operations

Dockerize the project for easier deployment

🤝 Contributing

Fork this repo

Create your feature branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add feature')

Push to branch (git push origin feature-name)

Open a Pull Request

📜 License

This project is licensed under the MIT License.
