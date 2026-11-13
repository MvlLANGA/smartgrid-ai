# SmartGrid AI

## Project Overview

SmartGrid AI is a Python-based power grid monitoring
and recovery simulation.

The project analyzes electrical network failures,
identifies disconnected power stations, finds
alternative routes, and recommends cable repairs
to restore energy availability.

## Key Features

•⁠  ⁠Power grid simulation
•⁠  ⁠Automatic cable failure detection
•⁠  ⁠Network connectivity analysis using BFS
•⁠  ⁠Identification of isolated power stations
•⁠  ⁠Alternative power route discovery
•⁠  ⁠Cable repair simulation
•⁠  ⁠Repair recommendation
•⁠  ⁠Energy recovery calculation
•⁠  ⁠Automated unit testing

## Technologies

•⁠  ⁠Python 3
•⁠  ⁠Graph Algorithms
•⁠  ⁠Breadth-First Search (BFS)
•⁠  ⁠Python Collections (deque)
•⁠  ⁠Unittest

## How to Run

### 1. Clone the Repository

⁠ bash
git clone <repository-url>
cd smartgrid-ai
 ⁠

### 2. Run the Simulation

⁠ bash
python3 solution.py
 ⁠

### 3. Run Automated Tests

⁠ bash
python3 -m unittest discover -s tests -v
 ⁠

## Example Results

The initial simulation contains four power stations
with a total of 50 energy units.

•⁠  ⁠Initial available energy: 30 units
•⁠  ⁠Initial unavailable energy: 20 units
•⁠  ⁠Initial energy loss: 40%
•⁠  ⁠Recommended repair: B-D
•⁠  ⁠Available energy after repair: 50 units
•⁠  ⁠Energy availability after repair: 100%

## Project Status

Core simulation implemented.
Three automated unit tests passing.