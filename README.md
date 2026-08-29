# Python by Example

A practical, example-driven Python repository designed to help you learn Python from fundamentals to advanced concepts through clear, runnable code.

Each file is self-contained and focuses on a single concept, making the repository suitable for structured learning, revision, or reference.

---

## Table of Contents

- [Overview](#-overview)
- [Topics Covered](#-topics-covered)
- [Getting Started](#-getting-started)
- [Prerequisites](#-prerequisites)
- [File Structure](#-file-structure)
- [Learning Path](#-learning-path)
- [Projects](#-projects)

---

## Overview

This repository contains a complete Python tutorial designed for both beginners and experienced developers looking to refresh their knowledge. Each topic is organized in separate folders with practical, runnable examples.

**Key Features:**
- ✅ **Self-contained files** — Each file can be run independently
- ✅ **Comprehensive comments** — Detailed explanations for every concept
- ✅ **Practical examples** — Real-world use cases and patterns
- ✅ **Progressive difficulty** — From basics to advanced topics

---

## Topics Covered

### 01. Basics
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_print.py`](./01_basics/01_print.py) | Print Function | Output, formatting, f-strings, escape characters |
| [`02_comments.py`](./01_basics/02_comments.py) | Comments | Single-line, multi-line, docstrings, best practices |
| [`03_variables.py`](./01_basics/03_variables.py) | Variables | Assignment, naming conventions, multiple assignment |
| [`04_data_types.py`](./01_basics/04_data_types.py) | Data Types | Numbers, strings, booleans, type conversion |

### 02. Control Flow
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_if_else.py`](./02_control_flow/01_if_else.py) | If/Else | Conditionals, comparison operators, logical operators |
| [`02_elif.py`](./02_control_flow/02_elif.py) | Elif | Multiple conditions, grading systems, ranges |
| [`03_match_case.py`](./02_control_flow/03_match_case.py) | Match/Case | Pattern matching (Python 3.10+), guards, unpacking |

### 03. Loops
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_for_loop.py`](./03_loops/01_for_loop.py) | For Loops | Iteration, range(), enumerate(), zip() |
| [`02_while_loop.py`](./03_loops/02_while_loop.py) | While Loops | Counters, sentinels, infinite loops |
| [`03_break_continue.py`](./03_loops/03_break_continue.py) | Loop Control | break, continue, pass, for-else |

### 04. Data Structures
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_lists.py`](./04_data_structures/01_lists.py) | Lists | Indexing, slicing, methods, comprehensions |
| [`02_tuples.py`](./04_data_structures/02_tuples.py) | Tuples | Immutability, unpacking, named tuples |
| [`03_sets.py`](./04_data_structures/03_sets.py) | Sets | Operations, frozen sets, practical uses |
| [`04_dictionaries.py`](./04_data_structures/04_dictionaries.py) | Dictionaries | Methods, nesting, comprehensions |

### 05. Functions
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_function_basics.py`](./05_functions/01_function_basics.py) | Function Basics | Defining functions, scope, docstrings |
| [`02_arguments.py`](./05_functions/02_arguments.py) | Arguments | Positional, keyword, *args, **kwargs, type hints |
| [`03_return_values.py`](./05_functions/03_return_values.py) | Return Values | Multiple returns, early returns, generators |
| [`04_lambda_functions.py`](./05_functions/04_lambda_functions.py) | Lambda | Anonymous functions, map, filter, reduce |

### 06. Modules & Packages
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_imports.py`](./06_modules_packages/01_imports.py) | Imports | Import patterns, standard library, organization |
| [`02_custom_modules.py`](./06_modules_packages/02_custom_modules.py) | Custom Modules | Creating modules, packages, `__init__.py` |

### 07. Error Handling
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_try_except.py`](./07_error_handling/01_try_except.py) | Try/Except | Exception handling, else, finally |
| [`02_custom_exceptions.py`](./07_error_handling/02_custom_exceptions.py) | Custom Exceptions | Creating exceptions, hierarchy, best practices |

### 08. Object-Oriented Programming
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_classes_objects.py`](./08_oop/01_classes_objects.py) | Classes & Objects | Attributes, methods, self |
| [`02_init_methods.py`](./08_oop/02_init_methods.py) | Init & Methods | Constructors, properties, classmethods |
| [`03_inheritance.py`](./08_oop/03_inheritance.py) | Inheritance | Single/multiple inheritance, super(), MRO |
| [`04_polymorphism.py`](./08_oop/04_polymorphism.py) | Polymorphism | Duck typing, operator overloading, protocols |

### 09. Advanced Python
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_list_comprehensions.py`](./09_advanced_python/01_list_comprehensions.py) | Comprehensions | List, dict, set comprehensions |
| [`02_generators.py`](./09_advanced_python/02_generators.py) | Generators | Yield, iterators, memory efficiency |
| [`03_decorators.py`](./09_advanced_python/03_decorators.py) | Decorators | Simple/parameterized decorators, functools |
| [`04_context_managers.py`](./09_advanced_python/04_context_managers.py) | Context Managers | with statement, `__enter__`/`__exit__`, contextlib |

### 10. Best Practices
| File | Topic | Description |
|:-----|:------|:------------|
| [`01_pep8.py`](./10_best_practices/01_pep8.py) | PEP 8 | Python style guide, naming, formatting |
| [`02_type_hinting.py`](./10_best_practices/02_type_hinting.py) | Type Hinting | Type annotations, typing module, generics |
| [`03_virtual_envs.py`](./10_best_practices/03_virtual_envs.py) | Virtual Environments | venv, pip, requirements.txt |

---

## Getting Started

Follow these steps to clone the repository and set it up in your local editor:

1. **Clone the repository**
   Open your terminal and run:
   ```bash
   git clone https://github.com/blshaer/python-by-example.git
   cd python-by-example
   ```

2. **Set up a Virtual Environment (Recommended)**
   It's best practice to keep your projects isolated. Run these commands:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   Install the necessary tools for testing and formatting:
   ```bash
   pip install -r requirements.txt
   ```

4. **Open in your code editor**
   We recommend [Visual Studio Code](https://code.visualstudio.com/). Open the project directly:
   ```bash
   code .
   ```

5. **Explore and Run**
   Navigate to any example, like `01_basics`, and run the file:
   ```bash
   cd 01_basics
   python 01_print.py
   ```

6. **Read the comments** — Detailed explanations are provided inline for every concept!

7. **Try the Tests** — Go to the new testing module to see how professional code is verified:
   ```bash
   pytest 11_testing/01_test_basics.py
   ```

---

## Prerequisites

| Requirement | Version | Notes |
|:------------|:--------|:------|
| Python | 3.10+ | Recommended (for match/case support) |
| Python | 3.8+ | Minimum (for most features) |

```bash
# Check your Python version
python --version
```

---

## File Structure

Each Python file follows a consistent structure:

```python
"""
================================================================================
File: filename.py
Topic: Topic Name
================================================================================

Description of what the file covers...

Key Concepts:
- Concept 1
- Concept 2
- ...

================================================================================
"""

# -----------------------------------------------------------------------------
# Section 1: Basic Example
# -----------------------------------------------------------------------------
# ... code with inline comments ...

# -----------------------------------------------------------------------------
# Section 2: Advanced Example
# -----------------------------------------------------------------------------
# ... more code ...
```

---

## Learning Path

<table>
<tr>
<td align="center"><strong>🌱 Beginner</strong></td>
<td align="center"><strong>📈 Intermediate</strong></td>
<td align="center"><strong>🚀 Advanced</strong></td>
<td align="center"><strong>💼 Professional</strong></td>
</tr>
<tr>
<td>

1. [Basics](./01_basics/)
2. [Control Flow](./02_control_flow/)
3. [Loops](./03_loops/)

</td>
<td>

4. [Data Structures](./04_data_structures/)
5. [Functions](./05_functions/)
6. [Modules](./06_modules_packages/)

</td>
<td>

7. [Error Handling](./07_error_handling/)
8. [OOP](./08_oop/)
9. [Advanced Python](./09_advanced_python/)

</td>
<td>

10. [Best Practices](./10_best_practices/)
11. [Testing](./11_testing/)

</td>
</tr>
</table>

```
 Recommended Flow:
Beginner     →  01_basics → 02_control_flow → 03_loops
Intermediate →  04_data_structures → 05_functions → 06_modules
Advanced     →  07_error_handling → 08_oop → 09_advanced
Professional →  10_best_practices → 11_testing
```

---

## Projects

Put your skills to the test! Each project includes a **challenge description** (`README.md`) so you can try building it yourself before looking at the solution.

| # | Project | Difficulty | Concepts Applied |
|:--|:--------|:-----------|:-----------------|
| 01 | [**Number Guessing Game**](./projects/01_number_guessing_game/) | 🟢 Beginner | Loops, Conditionals, Random module |
| 02 | [**Expense Tracker**](./projects/02_expense_tracker/) | 🟡 Intermediate | Dicts, File I/O (JSON), Functions |
| 03 | [**Library Management System**](./projects/03_library_management/) | 🟠 Advanced | OOP, Inheritance, Custom Exceptions |
| 04 | [**Real-time Weather CLI**](./projects/04_weather_cli/) | 🚀 Professional | API Requests, Decorators, Type Hints |

> 💡 **Tip:** Read the project `README.md` first and try to build it on your own before looking at `solution.py`!

---

## Progress Tracker

Use this checklist to track your learning progress:

- [ ] **01. Basics** — Print, Comments, Variables, Data Types
- [ ] **02. Control Flow** — If/Else, Elif, Match/Case
- [ ] **03. Loops** — For, While, Break/Continue
- [ ] **04. Data Structures** — Lists, Tuples, Sets, Dictionaries
- [ ] **05. Functions** — Basics, Arguments, Returns, Lambda
- [ ] **06. Modules & Packages** — Imports, Custom Modules
- [ ] **07. Error Handling** — Try/Except, Custom Exceptions
- [ ] **08. OOP** — Classes, Init, Inheritance, Polymorphism
- [ ] **09. Advanced Python** — Comprehensions, Generators, Decorators
- [ ] **10. Best Practices** — PEP8, Type Hints, Virtual Environments
- [ ] **11. Testing** — Unit Tests, Pytest, Assertions

### 🏗️ Projects
- [ ] **Project 01** — Number Guessing Game (Beginner)
- [ ] **Project 02** — Expense Tracker (Intermediate)
- [ ] **Project 03** — Library Management System (Advanced)
- [ ] **Project 04** — Real-time Weather CLI (Professional)

---

<p align="center">
  <strong>Happy Learning!</strong>
</p>

<p align="center">
  Made with ❤️ by <a href="https://github.com/blshaer">Baraa</a>
</p>
