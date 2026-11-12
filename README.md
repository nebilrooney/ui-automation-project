UI Automation Testing Project

Overview

This project contains automated UI tests for the SauceDemo website using Python and Playwright.

Tools & Technologies

- Python
- Playwright
- Pytest
- pytest-html

## Project Structure

```text
ui-automation-project/
├── pages/
│ ├── login_page.py
│ ├── products_page.py
│ └── cart_page.py
├── tests/
│ ├── test_login.py
│ ├── test_products.py
│ ├── test_cart.py
│ └── test_checkout.py
├── .gitignore
└── README.md
```


Test Coverage

- Valid and invalid login
- Products page validation
- Add and remove products from cart
- Cart validation
- Checkout process

Installation

python -m pip install pytest-playwright pytest-html
python -m playwright install chromium

Run Tests

python -m pytest -v tests

Generate HTML Report

python -m pytest -v --html=report.html --self-contained-html tests

Test Results: 9 tests passed.

