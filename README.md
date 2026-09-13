# Playwright Demo

An initial **Playwright automation framework design project** built using **Python, Pytest, and Playwright**.

The project demonstrates a basic and scalable structure for UI test automation, including page objects, test cases, configuration, and reusable components.

## 🚀 Tech Stack

* **Python**
* **Playwright**
* **Pytest**
* **Pytest-HTML** *(optional)*
* **Git**

## 📁 Project Structure

```text
playwright_demo/
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   └── config.py
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## ⚙️ Prerequisites

Make sure the following are installed:

* Python 3.9+
* Git
* VS Code or any preferred IDE

Check Python installation:

```bash
python --version
```

Check Git:

```bash
git --version
```

## 🔧 Installation

Clone the repository:

```bash
git clone <repository-url>
cd playwright_demo
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

**Git Bash:**

```bash
source venv/Scripts/activate
```

**PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_login.py
```

Run tests with verbose output:

```bash
pytest -v
```

## 🧪 Framework Approach

The framework follows the **Page Object Model (POM)** approach.

### Page Objects

Page-specific locators and actions are maintained inside the `pages` directory.

Example:

```python
class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.get_by_name("username")
        self.password = page.get_by_name("password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
```

### Tests

Test scenarios are maintained separately inside the `tests` directory.

This separation makes the framework easier to:

* Maintain
* Reuse
* Scale
* Debug
* Add new test scenarios

## 🌐 Demo Application

The initial automation is designed for the **OrangeHRM demo application**.

Application:

```text
https://opensource-demo.orangehrmlive.com/
```

The login automation covers:

* Opening the application
* Entering username
* Entering password
* Clicking Login
* Validating successful login

## 📊 Future Enhancements

The framework can be extended with:

* Browser configuration
* Headless/headed execution
* Environment-based configuration
* Fixtures
* Test data management
* Screenshots on failure
* Video recording
* Trace collection
* HTML reports
* Parallel execution
* Cross-browser testing
* CI/CD integration
* API automation
* Logging
* Retry mechanism

## 🔐 Git Ignore

The project ignores generated and sensitive files such as:

```text
__pycache__/
*.pyc
.pytest_cache/
.env
venv/
test-results/
playwright-report/
*.tmp
```

## 👨‍💻 Purpose

This project is an **initial Playwright framework design** intended to demonstrate a clean foundation for building maintainable and scalable Python-based UI automation.

---

**Playwright Demo — Python + Pytest + Playwright**
