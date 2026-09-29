# Modular Rock-Paper-Scissors Terminal Engine

A highly modular command-line game application built to demonstrate pure Python control flow, function packaging, and data structure mappings.

## Project Architecture
The engine consists of 5 files to preserve a strict separation of concerns:
- `config.py`: Game rule matrices and constant fields.
- `computr.py`: Randomized calculation engine handling opponent moves.
- `user_input.py`: Defensive user input text/numeric validation scripts.
- `game_logic.py`: Verification algorithms determining win/loss/tie outcomes.
- `main.py`: Operational orchestration center running the global match loop.

## Setup & Execution Guide

### Prerequisites
- Python 3.x installed on your operating system.

### Running the Application
1. Clone this public repository:
   ```bash
   git clone https://github.com{your-github-username}/{your-repo-name}.git
   ```
2. Navigate directly into the root folder:
   ```bash
   cd {your-repo-name}
   ```
3. Run the engine directly via your command terminal layout:
   ```bash
   python main.py
   ```

## Local Validation Testing
Verifyed that all game conditions pass manually by running validation inputs (e.g., entering letters when prompted for round counts, or entering arbitrary strings instead of game options) to confirm that the error-handling loops reset gracefully.
