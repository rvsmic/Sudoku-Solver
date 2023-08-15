# Sudoku Solver

![Python](https://img.shields.io/badge/python-3.x-green.svg)

Sudoku Solver is a simple Python application that solves Sudoku puzzles. It provides an easy-to-use interface for entering puzzles and obtaining their solutions.

## Table of Contents
- [Usage](#usage)
- [Installation](#installation)
- [Example](#example)

## Usage
1. Make sure you have Python 3.x installed on your system.
2. Clone this repository or download the source code.
3. Open a terminal and navigate to the project directory.

### Running the Solver
To run the solver, execute the following command in the terminal:

```bash
python3 sudoku_solver.py
```

The program will prompt you to enter the Sudoku puzzle. Enter the puzzle row by row, with each cell separated by a space. Empty spaces should be represented by a 0.


The program will then print the solved puzzle to the console.

## Installation

Clone this repository using:
```bash
git clone https://github.com/rvsmic/Sudoku-Solver.git
```

Navigate to the project directory:
```bash
cd sudoku-solver
```

## Example

Here's an example of how the Sudoku Solver works:

### Input:
```
0 0 0 2 6 0 7 0 1
6 8 0 0 7 0 0 9 0
1 9 0 0 0 4 5 0 0
8 2 0 1 0 0 0 4 0
0 0 4 6 0 2 9 0 0
0 5 0 0 0 3 0 2 8
0 0 9 3 0 0 0 7 4
0 4 0 0 5 0 0 3 6
7 0 3 0 1 8 0 0 0
```

### Output:
```
|-------|-------|-------|
| 4 3 5 | 2 6 9 | 7 8 1 |
| 6 8 2 | 5 7 1 | 4 9 3 |
| 1 9 7 | 8 3 4 | 5 6 2 |
|-------|-------|-------|
| 8 2 6 | 1 9 5 | 3 4 7 |
| 3 7 4 | 6 8 2 | 9 1 5 |
| 9 5 1 | 7 4 3 | 6 2 8 |
|-------|-------|-------|
| 5 1 9 | 3 2 6 | 8 7 4 |
| 2 4 8 | 9 5 7 | 1 3 6 |
| 7 6 3 | 4 1 8 | 2 5 9 |
|-------|-------|-------|
```