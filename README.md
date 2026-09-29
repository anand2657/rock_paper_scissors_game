## 📝 Project Description

The **Modular Rock-Paper-Scissors Terminal Engine** is a lightweight, decoupled command-line application engineered to showcase fundamental principles of structured programming and computer science logic in Python. 

While classic text games are traditionally condensed into single, monolithic scripts, this engine serves as an architectural exercise in **Separation of Concerns (SoC)**. By isolating system configuration, input parsing, randomized movement generation, and game loop orchestration into five independent scripts, the codebase avoids "spaghetti code" and scales cleanly into a production-ready command line interface (CLI).

---

## 🏗️ Core Architectural Modules

The engine relies on a multi-module footprint to isolate tasks and ensure clean execution paths:

*   **`config.py` (Data & Rule Layer):** Establishes the immutable rules of the game. It uses a Python collection list to lock game choices (`OPTIONS`) and a structured hash-map lookup dictionary (`WINNING_PAIRS`) to map item superiorities directly.
*   **`user_input.py` (Defensive Input Processor):** Guards runtime loops against dirty user data. It implements isolated `while True` sequences combined with structured `try-except ValueError` blocks to seamlessly capture malformed string entries or out-of-bounds numbers without crashing.
*   **`computr.py` (Decision Automation Engine):** Drives computer behavior using standard library pseudo-random algorithms (`random.choice`). It samples choices dynamically across a uniform distribution to guarantee unbiased computer tactical moves.
*   **`game_logic.py` (Computational Matrix Evaluator):** Eliminates messy conditional statements. Instead of nesting multiple `if-else` blocks, it evaluates winning outcomes instantly via an \(\mathcal{O}(1)\) dictionary hash lookup, updates local session registers, and outputs real-time match results.
*   **`main.py` (Central System Orchestrator):** Controls the life cycle of the match. It links variables across modules, manages state counters, keeps scores, and runs cleanly using terminal execution workflows.

---

## ⚡ Key Computational Features

*   **\(\mathcal{O}(1)\) Decision Matrix:** Winning determinations bypass nested branching logic, utilizing immediate key-value lookup queries on predefined rule sets.
*   **Data Sanitization Pipe:** String entries undergo comprehensive formatting adjustments (`.lower().strip()`) to allow flexible user responses without triggering logic breaks.
*   **Path Resolution Independent:** Employs explicit runtime search path injection (`sys.path.append`), guaranteeing smooth cross-module importing across different operating system environments and terminal consoles.
