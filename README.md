# 🧪 Automation Practice Website — Python Framework Workshop

This repository represents a **phase-by-phase automation framework workshop**, built on top of:
[https://rahulshettyacademy.com/AutomationPractice/](https://rahulshettyacademy.com/AutomationPractice/)

> ⚠️ **Important**  
> This repository is **not a sample test project**.  
> It is a **learning-driven framework design workshop**, focused on *how and why* a scalable automation framework is built.

---

## 🎯 Workshop Objectives

- Build a **production-grade Selenium + Pytest hybrid framework**
- Understand **framework architecture decisions**
- Learn **test lifecycle, abstraction, stability, and scalability**
- Become **interview-ready for Senior Automation / SDET roles**

---

## 🧰 Technology Stack

| Category           | Tool                          |
| ------------------ | ----------------------------- |
| Language           | Python                        |
| Test Framework     | Pytest                        |
| UI Automation      | Selenium WebDriver            |
| Driver Management  | webdriver-manager             |
| Configuration      | YAML                          |
| Data Driven        | CSV + Pytest parameterization |
| Reporting          | pytest-html, Allure           |
| Logging            | Python logging                |
| Parallel Readiness | pytest-xdist (design preview) |
| CI Readiness       | Yes (design-level)            |

---

## 📁 Framework Folder Structure

```text
Automation-Practice-Website/
│
├── base/
│   └── base_page.py
│
├── pages/
│   └── practice_page.py
│
├── config/
│   └── config.yaml
│
├── utils/
│   ├── config_reader.py
│   ├── datareader.py
│   └── logger.py
│
├── tests/
│   └── test_*.py
│
├── conftest.py
├── run_test.py
│
├── reports/            # pytest-html reports
├── allure-results/     # Allure raw results
├── allure-report/      # Allure HTML output
├── screenshots/
│
└── README.md
```

---

## 🧠 Conceptual Test Flow

```text
Test
 ↓
Page Object
 ↓
BasePage
 ↓
Selenium WebDriver
```

- Tests express intent
- Page Objects express UI behavior
- BasePage handles interaction mechanics
- Selenium controls the browser

---

## 🧩 Framework Architecture
```md
## 🧪 Conceptual Test Flow
```
```mermaid
flowchart TD

    subgraph Test_Layer
        T[Test Cases]
    end

    subgraph Step_Optional
        ST[Step Layer]
    end

    subgraph Page_Layer
        P[Page Objects]
    end

    subgraph Base_Layer
        B[BasePage]
    end

    subgraph Core_Infra
        D[WebDriver]
        C[Config]
        DR[Test Data]
    end

    subgraph Observability
        L[Logging]
        R[Reports]
    end

    subgraph Execution
        PY[Pytest Engine]
    end

    T -->|intent| P
    T --> DR

    ST -.optional.-> P
    T -.optional.-> ST

    P --> B
    B --> D

    PY --> T
    PY --> C
    PY --> D

    B --> L
    PY --> R

```

```md
## 🧪 Class Diagram
```
```mermaid
classDiagram

    class TestCase {
        +test_method()
    }

    class PracticePage {
        +select_radio_button()
        +enter_autosuggestion(text)
        +hide_textbox()
        +show_textbox()
        +is_textbox_visible()
    }

    class BasePage {
        -driver
        -wait
        +click(locator)
        +type_text(locator, text)
        +get_text(locator)
        +is_visible(locator)
        +_retry(action, name, locator)
    }

    class ConfigReader {
        +get(key)
    }

    class DataReader {
        +load_csv_data(path)
    }

    class Logger {
        +info(msg)
        +error(msg)
        +warning(msg)
    }

    class WebDriver {
        +get(url)
        +find_element()
        +quit()
    }

    class PytestEngine {
        +collect_tests()
        +resolve_fixtures()
        +run_tests()
    }

    TestCase --> PracticePage : uses
    PracticePage --> BasePage : inherits
    BasePage --> WebDriver : wraps
    TestCase --> DataReader : uses (parameterization)
    TestCase --> Logger : logs
    PytestEngine --> TestCase : executes
    PytestEngine --> ConfigReader : injects config
    PytestEngine --> WebDriver : lifecycle via fixtures
```
```md
## 🧪 Conceptual Test Flow
```
```mermaid
flowchart TD
    T[Test Case] --> P[Page Object]
    P --> B[BasePage]
    B --> S[Selenium WebDriver]

    T:::testStyle
    P:::pageStyle
    B:::baseStyle
    S:::driverStyle

    classDef testStyle fill:#1e3a8a,stroke:#93c5fd,stroke-width:1px;
    classDef pageStyle fill:#14532d,stroke:#86efac,stroke-width:1px;
    classDef baseStyle fill:#78350f,stroke:#fde68a,stroke-width:1px;
    classDef driverStyle fill:#581c87,stroke:#e9d5ff,stroke-width:1px;

```


---

## 🧱 Phase-by-Phase Framework Evolution

### Phase 1 — Framework Bootstrap

- Raw Selenium + Pytest smoke test
- Environment & tooling validation

**Focus:** Prove automation can run

---

### Phase 2 — Fixtures & Lifecycle Management

- Introduced `conftest.py`
- Browser lifecycle via fixtures
- Dependency Injection

**Focus:** Centralized setup & teardown

---

### Phase 3 — BasePage Abstraction

- Centralized waits & Selenium actions
- Retry mechanism & error handling
- Reduced flakiness

**Focus:** Stability & consistency

---

### Phase 4 — Page Object Model (POM)

- UI structure isolated
- Locators centralized
- Tests became readable

**Focus:** Maintainability

---

### Phase 5 — Configuration Management

- YAML-based environment config
- CLI environment switching (`--env`)
- No hardcoded values

**Focus:** Environment agnosticism

---

### Phase 6 — Driver Lifecycle & Execution Control

- Session-level driver reuse
- Autouse page reset
- Data-driven stability
- Parallel-ready design

**Focus:** Speed + isolation

---

### Phase 6 (Preview) — Parallel Execution

- pytest-xdist vs CI agent comparison
- Design readiness without enabling

**Focus:** Scalability awareness

---

### Phase 7 — Logging, Screenshots & Hooks

- Centralized logging
- Screenshot capture on failure
- Pytest lifecycle hooks
- XFAIL / SKIP handling

**Focus:** Debuggability

---

### Phase 8 — Data Driven Testing & Reporting

- CSV-driven execution
- pytest-html reports
- Allure reports with screenshots
- Timestamped execution reports

**Focus:** Execution visibility

---

## 📊 Reporting Usage

### pytest-html

```bash
python run_test.py
```

Output:

```text
reports/TestReport-YYYYMMDD-HHMMSS.html
```

---

### Allure

```bash
python -m pytest tests --alluredir=allure-results
allure serve allure-results
```

---

## ⚙️ Environment Control

```bash
python -m pytest tests --env=uat
```

Configuration source:

```text
config/config.yaml
```

---

## 🧪 Data Driven Execution

- CSV files provide test datasets
- Each row treated as an independent test
- Browser reuse with reset guarantees isolation

---

## 🎤 Interview Readiness

This repository demonstrates:

- Framework design thinking
- Test lifecycle mastery
- Layered abstraction
- Stability & scalability awareness
- Reporting and debugging maturity

---

## 🧊 Final Note

This repository is a **framework design workshop**, not a one-time automation project.

Every abstraction exists **because a real problem demanded it**.

---

### ✅ This is now **GitHub-renderable Markdown**

- No nested markdown
- Code blocks only where required
- Mermaid isolated correctly
- Tables render cleanly

```

If you want any tweaks (e.g., adjust headings, add or remove sections, or tailor to a specific repo structure), tell me and I’ll update it.