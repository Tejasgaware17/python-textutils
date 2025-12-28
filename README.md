# textutils

A small, installable Python package built to deeply understand **Python modules, packages, and imports** using professional development practices.

This project is **intentionally minimal** in features but complete in concepts.

---

## 🎯 Purpose

The goal of this project is to gain a **clear and correct mental model** of:

- Python modules vs packages
- Absolute vs relative imports
- `__init__.py` and package namespaces
- `__all__` and public APIs
- `python -m` execution
- Installable packages using `pyproject.toml`
- Editable installs (`pip install -e .`)
- Isolated development with virtual environments
- Proper testing imports with `pytest`

---

## 📦 Package Structure

```bash
textutils_project/
│
├── textutils/
│ ├── init.py
│ ├── cleaner.py
│ └── analyzer.py
│
├── tests/
│ └── test_cleaner.py
│
├── pyproject.toml
├── README.md
├── main.py
└── .gitignore
```

---

## 🚀 Installation (development mode)

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
pip install -e .
```

This installs the package in editable mode inside an isolated environment.

---

## 🧪 Running Tests

```bash
pytest
```

Tests import the package the same way end users do — no path hacks.

---

## 🧠 Key Learning Takeaways

- File paths do not define package context — execution mode does
- Relative imports depend on `__package__`, not `sys.path`
- `python -m` is required for running package modules correctly
- Installing a package removes dependency on the project root
- Tests should import packages exactly like real consumers

---

## 📌 Why this project exists

This repository demonstrates how real Python libraries are structured, executed, tested, and versioned — even at a small scale.

The focus is on correctness, clarity, and professional workflow rather than unwanted complexity.
