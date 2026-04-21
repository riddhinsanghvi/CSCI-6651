# CSCI-6651: Introduction to Python Scripting

**University of New Haven**
**MS Cybersecurity Program**

This repository contains all assignments, quizzes, midterms, and the final exam for CSCI-6651: Introduction to Python Scripting. Each submission demonstrates core Python programming concepts progressively built across the semester.

---

## Repository Structure

```
CSCI-6651/
├── Assignment 1/       # Python strings and immutability
├── Assignment 2/       # Recursion and string permutations
├── Assignment 3/       # Lists, data structures (stack/queue), and string manipulation
├── Assignment 4/       # 3D point input, float validation, and distance computation
├── Assignment 5/       # Caesar cipher and frequency analysis
├── Assignment 6/       # User account management system
├── Assignment 7/       # File I/O and packet validation (procedural)
├── Assignment 8/       # File I/O and packet validation (OOP refactor)
├── Mid term/           # Midterm exam solutions
├── Quiz/               # In-class quiz solutions including Hangman
├── Final Exam/         # Battleship game with OOP, file persistence, and unit tests
└── Textbook/           # Python Crash Course (Eric Matthes)
```

---

## Assignments

### Assignment 1 - Python Strings and Immutability
Explores Python string behavior, object identity (`id()`), and the immutability of strings. Demonstrates how concatenation creates a new string object rather than modifying the original.

**Concepts:** string immutability, object identity, type inspection

### Assignment 2 - String Permutations
An interactive program that accepts alphabetic input from the user and generates all unique permutations using a recursive algorithm. Applies a consonant-vowel-consonant (CVC) heuristic to identify "possible words."

**Concepts:** recursion, permutations, input validation, heuristic filtering

### Assignment 3 - Lists and Data Structures
A multi-part assignment covering:
- Collecting numeric user input into a list with validation
- Character frequency counting in a string
- String reversal using slicing
- A dual-mode data structure supporting both FIFO (queue) and LIFO (stack) operations

**Concepts:** lists, dictionaries, string slicing, FIFO/LIFO

### Assignment 4 - 3D Points and Distance Computation
Accepts named 3D coordinate points `(x, y, z)` from the user with float validation and a quit option. Computes and displays Euclidean distances between all entered points.

**Concepts:** tuples, float validation, 3D geometry, input loops

### Assignment 5 - Caesar Cipher Decryption
Performs frequency analysis on a Caesar-ciphertext string and decrypts it by trying all 26 possible shifts. Implements the cipher logic from scratch without built-in shift functions.

**Concepts:** Caesar cipher, character frequency analysis, modular arithmetic, brute-force decryption

### Assignment 6 - User Account Management
A console-based user registration system that enforces non-empty fields, unique usernames (case-insensitive), and matching password confirmation. Stores accepted accounts in a list of dictionaries and masks passwords on display.

**Concepts:** dictionaries, input validation, password handling, list management

### Assignment 7 - Network Packet Validator (Procedural)
Reads a `.txt` file of simulated network packets, validates each packet's format (numeric value followed by CRLF), decodes valid packets to float values, and writes results to an output file.

**Concepts:** file I/O, string parsing, CRLF handling, format validation

### Assignment 8 - Network Packet Validator (OOP Refactor)
Refactors Assignment 7 into an object-oriented design using two classes:
- `Packet`: encapsulates a single packet with validation and decoding methods
- `PacketFileProcess`: handles file reading, packet processing, and output writing

**Concepts:** OOP, class design, encapsulation, file I/O

---

## Midterm

Three midterm problems building on prior assignments, including a revised user account system using tuples instead of dictionaries, and an input validation system using an `Elements` class with min/max range checking.

---

## Quizzes

| Quiz | Description |
|------|-------------|
| Quiz 5 | `Elements` class with validated range input |
| Quiz 6 | Extended quiz problems |
| Q6, Q7, Q8 | Additional in-class quiz solutions |
| Hangman | A fully modular Hangman game split across multiple files: `game.py`, `player.py`, `word.py`, `figure.py`, `guesses.py`, `main.py` |

---

## Final Exam - Battleship Game

A fully featured, object-oriented Battleship game played on a 26x10 grid (rows A-Z, columns 1-10).

**Ship Types:**

| Ship | Length | Count |
|------|--------|-------|
| Destroyer | 3 | 2 |
| Cruiser | 5 | 1 |
| Battleship | 7 | 1 |
| Aircraft Carrier | 9 | 1 |

**Features:**
- OOP design with classes for ships, boards, game state, and players
- Coordinate system using letter-number notation (e.g., `A5`, `Z10`)
- Persistent game records saved and loaded via JSON (`battleship_records.json`)
- Full unit test suite covering board logic, ship placement, and game flow

**Test Files:**
- `test_board.py`
- `test_ship.py`
- `test_game.py`
- `test_system.py`

---

## Technologies

- **Language:** Python 3
- **Libraries:** `json`, `os`, `datetime`, `typing`
- **Testing:** `unittest` (pytest-compatible)
- **Tools:** No external dependencies required

---

## How to Run

### Run any assignment
```bash
python "Assignment X/Riddhi_Sanghvi-AssignmentX.py"
```

### Run the Final Exam (Battleship)
```bash
cd "Final Exam"
python Riddhi_Sanghvi_Final_Exam.py
```

### Run unit tests
```bash
cd "Final Exam"
python -m pytest
```

---

## Author

**Riddhi Sanghvi**
MS Cybersecurity, University of New Haven
