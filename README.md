# Martian Robots

This is a small command-line solution for the Martian Robots coding challenge.

I kept the project deliberately simple: read the input from stdin, process the
robots in order, and print the final state for each robot. There is no UI or
extra framework because the interesting part of the task is the movement logic
and the scent behaviour.

## How I approached it

The code is split into a few small modules:

- `Robot` holds a robot's position, direction, instructions, and lost state.
- `World` holds the grid size and any scents left by lost robots.
- `parser` turns the input lines into robot objects.
- `simulator` applies the movement rules.
- `main.py` wires stdin, parsing, simulation, and stdout together.

The shared `World` object matters because robots are processed one after the
other. If one robot is lost, its scent must be available when the next robot
runs.

## Tech choices

The app only needs Python's standard library at runtime.

I used `pytest` for tests because it is lightweight and easy to read. The
project metadata lives in `pyproject.toml`, which also defines a small optional
console command.

## Requirements

- Python 3.10 or newer
- `pytest` for running tests

## Setup

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the project and test dependency:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

Using the sample input:

```bash
python main.py < sample.txt
```

Or, after installing the project:

```bash
martian-robots < sample.txt
```

Expected output:

```text
1 1 E
3 3 N LOST
2 3 S
```

## Input

The first line is the upper-right coordinate of the world:

```text
5 3
```

Each robot then has two lines:

```text
1 1 E
RFRFRFRF
```

The first line is `x y direction`. The second line is the instruction string.

Supported instructions:

- `L` turns left
- `R` turns right
- `F` moves forward

I have assumed the input follows the challenge constraints: coordinates are no
greater than `50`, and instruction strings are shorter than `100` characters.

## Test

Run:

```bash
python -m pytest
```

The tests cover parsing, direction changes, movement, lost robots, scents, and
the full sample input/output path.

## Notes

I have not added a separate validation layer. The challenge describes the input
format and constraints, so I treated the input as valid and kept the solution
focused on the movement and scent rules.

If this were going to be used outside the challenge, I would add clearer error
messages for malformed input, invalid directions, and out-of-range coordinates.
