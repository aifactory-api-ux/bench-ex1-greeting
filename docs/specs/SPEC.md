# SPEC.md

## 1. TECHNOLOGY STACK

| Layer | Technology | Version / Detail |
|---|---|---|
| Language | Python | 3.11 (CPython 3.11.x) |
| Test framework | `unittest` | Python standard library, no external package |
| Test runner | `unittest discover` | `python -m unittest discover tests` |
| Runtime dependencies | None | Zero third-party packages required |
| Build system | None | Pure Python source files, no packaging/docker/build required |
| Frontend | None | No frontend framework, no HTML/JS/CSS |
| Database | None | No persistence, no cache, no ORM |
| HTTP framework | None | No HTTP server, no FastAPI/Flask/Django |
| Message queue | None | No background jobs, no brokers |
| External services | None | No API keys, no network calls |

The original requirement describes a **pequeña y autónoma** utility. Therefore the only runtime dependency is the Python standard library, and the only execution model is local import or direct Python invocation.

---

## 2. DATA CONTRACTS

There are **no persistent data models** in this utility. No database table, Pydantic model, TypeScript interface, enum, or class is required.

The sole data contract is the public function signature and its input/output behavior.

### 2.1 Function Contract

```python
def greet(name: str) -> str:
```

| Contract Element | Exact Value |
|---|---|
| Module path | `src.greeting` |
| Function name | `greet` |
| Input name | `name` |
| Input type | `str` |
| Output type | `str` |
| Public API | Yes, exported from `src/greeting.py` |
| Side effects | None |
| Dependencies | None — only Python `str.strip()`, `str.__bool__`, and f-string formatting |

### 2.2 Algorithm Contract

The implementation MUST follow this exact algorithm:

1. Apply `name.strip()` to remove all leading and trailing whitespace from `name`.
2. If the stripped result is empty, return the exact string `"Hello, World!"`.
3. If the stripped result is not empty, return the exact string `` f"Hello, {stripped_name}!" `` where `stripped_name` is the value from step 1.

The function MUST NOT modify `name` in place; strings are immutable and no external state is written.

### 2.3 Input/Output Behavior Table

| Input | Stripped Value | Return Value |
|---|---|---|
| `"Alice"` | `"Alice"` | `"Hello, Alice!"` |
| `"  Alice"` | `"Alice"` | `"Hello, Alice!"` |
| `"Alice  "` | `"Alice"` | `"Hello, Alice!"` |
| `"  Alice  "` | `"Alice"` | `"Hello, Alice!"` |
| `""` | `""` | `"Hello, World!"` |
| `"   "` | `""` | `"Hello, World!"` |
| `"\tAlice\n"` | `"Alice"` | `"Hello, Alice!"` |

The last row is a direct consequence of Python's `str.strip()` behavior; no additional Unicode normalization or special character handling is required beyond `str.strip()`.

### 2.4 Expected Test Assertions

The test file MUST assert these exact expected values:

| Test Input | Expected `greet` Output |
|---|---|
| `"Alice"` | `"Hello, Alice!"` |
| `"  Alice  "` | `"Hello, Alice!"` |
| `""` | `"Hello, World!"` |

No test for explicit whitespace-only input is required by the original three-test requirement, but the implementation naturally handles it.

---

## 3. API ENDPOINTS

| Method | Path | Request Body | Response Body | Description |
|---|---|---|---|---|
| _none_ | _none_ | _none_ | _none_ | No HTTP API is required by this specification. |

The only interface is an **importable Python function** called `greet`. It is consumed as:

```python
from src.greeting import greet

result = greet(" Alice ")
```

No REST, GraphQL, gRPC, CLI argument parsing, or webhook endpoints are in scope. The utility is fully local and synchronous.

---

## 4. FILE STRUCTURE

```
.
├── README.md
├── src/
│   └── greeting.py
└── tests/
    └── test_greeting.py
```

### 4.1 File Descriptions

| File | Description |
|---|---|
| `README.md` | Brief Markdown file explaining the utility. MUST contain instructions for running the function and for running the automated test suite. No extra sections are required. |
| `src/greeting.py` | Contains the public function `greet(name: str) -> str`. The file MUST be importable using `from src.greeting import greet`. It MUST NOT contain an `if __name__ == "__main__":` entry point, side effects, network calls, or file I/O. |
| `tests/test_greeting.py` | Contains a `unittest.TestCase` class named `TestGreeting` with exactly three test methods: `test_normal_name`, `test_name_with_spaces`, and `test_empty_string`. |

No `src/__init__.py` is required because Python 3.3+ supports implicit namespace packages, and executing tests from the repository root places the root directory on `sys.path`.

### 4.2 File Tree with Descriptions

```text
.
├── README.md
│     Brief usage/run documentation.
├── src/
│   └── greeting.py
│         Public function `greet(name: str) -> str`.
│         Implements strip, empty fallback, and greeting formatting.
└── tests/
    └── test_greeting.py
          Unit tests for normal name, spaced name, and empty string.
```

### 4.3 Port Table

Not applicable. This project creates no network listeners, containers, or services.

### 4.4 Shared Modules

Not applicable. Only one production module exists, imported directly by the test module.

---

## 5. ENVIRONMENT VARIABLES

| Name | Type | Description | Example |
|---|---|---|---|
| _none_ | _none_ | No environment variables are defined, consumed, or required by this utility. | _none_ |

The utility MUST run without any environment configuration. It MUST NOT read `os.environ`, `.env` files, or external configuration files.

---

## 6. IMPORT CONTRACTS

### 6.1 Production Exports

The only authorized import contract is:

```python
from src.greeting import greet
```

| Module | Export Name | Type | Description |
|---|---|---|---|
| `src.greeting` | `greet` | `Callable[[str], str]` | Public greeting function |

`greet` MUST be defined at module level with the exact signature:

```python
def greet(name: str) -> str:
```

No other functions, classes, constants, or aliases are part of the contract.

### 6.2 Test Imports

`tests/test_greeting.py` MUST use:

```python
import unittest

from src.greeting import greet
```

The test file MUST NOT use relative imports such as `from ..src.greeting import greet`, because the tests run from the repository root with `unittest discover`.

### 6.3 Internal Imports

`src/greeting.py` MUST NOT import any module other than the Python standard library it requires for its logic. In the minimal implementation it requires no imports at all.

---

## 7. FRONTEND STATE & COMPONENT CONTRACTS

| Contract Type | Name | Type | Description |
|---|---|---|---|
| React hook | _none_ | _none_ | No frontend framework is used. |
| Vue composable | _none_ | _none_ | No frontend framework is used. |
| Angular service | _none_ | _none_ | No frontend framework is used. |
| Svelte store | _none_ | _none_ | No frontend framework is used. |
| Reusable component | _none_ | _none_ | No UI components are required. |

This is a Python-only utility. There is no frontend package, no `package.json`, no bundler, no browser entry point, and no DOM interaction.

---

## 8. FILE EXTENSION CONVENTION

| Item | Convention |
|---|---|
| Project language | Python |
| Is project JavaScript/TypeScript? | No |
| Production source extension | `.py` |
| Test source extension | `.py` |
| Frontend extension | Not applicable — no `.jsx`, `.tsx`, `.js`, `.ts`, `.vue`, `.svelte` files |
| Entry point as in `index.html` `<script src>` | Not applicable — no `index.html` exists |
| Python import entry point | `src.greeting:greet` |
| Test entry point | `python -m unittest discover tests` (run from repository root) |
| Example invocation | `python -c "from src.greeting import greet; print(greet(' Alice '))"` |

The `src` directory is treated as an implicit namespace package. Do not create `src/__init__.py`; it is not required.

---

## 9. DESIGN TOKENS

Not applicable. No UI/UX Design Implementation Contract exists in the provided project context. There is no frontend, and therefore no `frontend/src/styles/tokens.ts`, no color palette, no typography tokens, no spacing scale, no border radii, and no shadow tokens are defined or imported.

---

## 10. FUNCTIONAL REQUIREMENTS COVERAGE

| Requirement | Implementation | Files |
|---|---|---|
| Create the file `src/greeting.py` | A Python module MUST be created at the exact path `src/greeting.py` | `src/greeting.py` |
| Provide a public function named `greet` | Define `def greet(name: str) -> str:` at module level; no underscore prefix, no class wrapper | `src/greeting.py` |
| Function accepts `name` of type `str` | Parameter annotated as `name: str` | `src/greeting.py` |
| Function returns a `str` | Return type annotated as `-> str` | `src/greeting.py` |
| Remove leading and trailing spaces from `name` | Use `stripped_name = name.strip()` before emptiness check | `src/greeting.py` |
| Return `"Hello, <name>!"` when the stripped value is non-empty | Use `return f"Hello, {stripped_name}!"` when `stripped_name` is truthy/non-empty | `src/greeting.py` |
| Use `"World"` when the stripped value is empty | Use `return "Hello, World!"` when `stripped_name == ""` or if stripped value is empty | `src/greeting.py` |
| Create `tests/test_greeting.py` | Add `unittest.TestCase` class and three test methods | `tests/test_greeting.py` |
| Test a normal name | `test_normal_name` asserts `greet("Alice") == "Hello, Alice!"` | `tests/test_greeting.py` |
| Test a name with spaces | `test_name_with_spaces` asserts `greet("  Alice  ") == "Hello, Alice!"` | `tests/test_greeting.py` |
| Test an empty string | `test_empty_string` asserts `greet("") == "Hello, World!"` | `tests/test_greeting.py` |
| Include a brief `README.md` with usage instructions | README MUST document how to run the function and how to run the tests; e.g., `python -m unittest discover tests` and `python -c "from src.greeting import greet; print(greet(' Alice '))"` | `README.md` |
| Keep the utility autonomous | Implement with no third-party packages, no environment variables, no network calls, no file I/O, and no external services | `src/greeting.py` |
| Keep the workspace scope minimal | Create exactly `README.md`, `src/greeting.py`, and `tests/test_greeting.py`; no extra infrastructure | all files |

### 10.1 Explicit Test Contract

`tests/test_greeting.py` MUST contain the following exact test class and method logic:

```python
import unittest

from src.greeting import greet


class TestGreeting(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_name_with_spaces(self):
        self.assertEqual(greet("  Alice  "), "Hello, Alice!")

    def test_empty_string(self):
        self.assertEqual(greet(""), "Hello, World!")
```

The test order does not matter, but the method names MUST be used verbatim as above.

### 10.2 README Content Contract

`README.md` MUST be brief and MUST include at least the following two pieces of information:

1. How to run the function:
   ```bash
   python -c "from src.greeting import greet; print(greet(' Alice '))"
   ```

2. How to run the tests:
   ```bash
   python -m unittest discover tests
   ```

No other README sections are required by the original request, but additional brief explanation may be added without introducing new requirements.