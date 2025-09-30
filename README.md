# AI_AGENT 🧠⚡

An intelligent AI Agent project built with Python, featuring a modular architecture and an integrated Calculator module with both CLI and Tkinter UI support.

---

## 📂 Project Structure

```
AI_AGENT/
├── call_function.py       # Function caller module for AI agent
├── config.py              # Configurations and constants
├── functions/             # Utility functions directory
├── main.py                # Entry point for AI Agent
├── tests.py               # Unit tests
├── pyproject.toml         # Project metadata
├── uv.lock                # Lock file for dependencies
├── README.md              # Documentation
│
└── calculator/            # Calculator module
    ├── calculator.py      # CLI calculator
    ├── calculator_ui.py   # Tkinter UI calculator
    ├── main.py            # Entry point for calculator
    ├── tests.py           # Calculator tests
    ├── README.md          # Sub-project README
    ├── Bill.txt           # Sample data
    ├── lorem.txt          # Sample text file
    ├── text/              # Text assets
    │   └── text.txt
    └── pkg/               # Supporting package files
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Anand3074/AI_AGENT.git
cd AI_AGENT
```

### 2. Create a Virtual Environment

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` isn't available, install dependencies manually as needed (e.g., `tkinter`).

---

## 🧑‍💻 Running the AI Agent

Launch the main agent:

```bash
python main.py
```

The agent uses `call_function.py`, the `functions/` directory, and `config.py` to process tasks dynamically.

---

## 🖩 Running the Calculator

### CLI Calculator

Navigate to the calculator directory and run:

```bash
cd calculator
python calculator.py "2 + 3 * (4 - 1)"
```

### Tkinter UI Calculator

Launch the graphical interface:

```bash
cd calculator
python calculator_ui.py
```

A GUI window will open where you can type mathematical expressions and see results instantly.

---

## 🧪 Running Tests

Execute all tests using pytest:

```bash
pytest
```

Tests are available for both the AI Agent and the Calculator module.

---

## 📖 Features

### AI Agent
- **Function calling system** via `call_function.py`
- **Modular architecture** with organized `functions/` directory
- **Configurable setup** through `config.py`
- **Extensible design** for adding new capabilities

### Calculator
- **CLI calculator** with expression evaluation
- **Tkinter-based GUI** for interactive use
- **Sample data files** for testing and demonstration
- **Supports** basic arithmetic operations and parentheses

---

## 📌 Future Improvements

- [ ] Add more advanced AI agent functions
- [ ] Expand calculator to support scientific operations (sin, cos, log, etc.)
- [ ] Implement history tracking for calculations
- [ ] Dockerize the project for easier deployment
- [ ] Add API endpoints for remote agent interaction
- [ ] Enhance UI with modern styling and themes

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork** this repository
2. **Create** your feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add feature: description'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature-name
   ```
5. **Open** a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---


<div align="center">
  <sub>Built with ❤️ using Python</sub>
</div>
