
# Demo QA Testing

Hi — I'm learning test automation. This repo has a few simple Selenium tests I wrote while practicing.

What is here

- Basic pytest tests: alerts, browser windows, and a form submission.

Prerequisites

- Python installed (3.8+)
- A terminal (PowerShell or cmd)

Quick setup (Windows)

1. Make a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install the tools I used:

```powershell
python -m pip install --upgrade pip
python -m pip install pytest selenium webdriver-manager
```

Run tests

```powershell
python -m pytest
```

Run a single file:

```powershell
python -m pytest test_form_submission.py
```

Notes

- I used `webdriver-manager` so you usually don't need to download browser drivers yourself.
- These tests were written for learning — they may need tweaks on different browsers or OS versions.
- If installs fail, try `python -m pip install --upgrade pip setuptools wheel` and then retry.

If you want, I can make this even simpler or add a `requirements.txt`.
