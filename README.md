# Genetic Algorithm for Exam Timetabling

A genetic algorithm implementation for solving the exam timetabling problem using the Toronto benchmark dataset.

## Problem Description

The exam timetabling problem involves scheduling exams for students while satisfying various constraints:

**Hard Constraints:**
- No student can have two exams scheduled at the same time
- Each exam must be assigned to exactly one timeslot

**Soft Constraints (penalties):**
- Exams scheduled close together should be avoided
- Distance penalties:
  - Adjacent slots (distance=1): penalty of 8
  - Distance=2: penalty of 4
  - Distance=3: penalty of 2
  - Distance=4: penalty of 1

## Dataset

**Toronto Benchmark - ear-f-83-3.stu**
- Students: 1108
- Exams: 189
- Available timeslots: 30

Source: [University of Nottingham Benchmark Data Sets](https://www.cs.nott.ac.uk/~pszrq/data.htm)

## Chromosome Encoding

**Representation:** Direct encoding as a list of integers
- Length: 189 (number of exams)
- Each index represents an exam (0-indexed)
- Each value represents the assigned timeslot (0-29)

Example: `[5, 12, 3, ...]` means:
- Exam 0 → Timeslot 5
- Exam 1 → Timeslot 12
- Exam 2 → Timeslot 3

**Design rationale:** Direct encoding is simple, interpretable, and allows standard genetic operators to work naturally.

## Fitness Function

The fitness function minimizes the total penalty across all students:

```
fitness = -1 * (total_penalty / num_students)
```

Where `total_penalty` is calculated by:
1. For each student, check all pairs of their exams
2. Calculate distance between timeslots
3. Apply penalty based on distance (16 for same-slot, 8 for adjacent, etc.)

**Note:** Currently same-slot conflicts receive penalty of 16, but this should be increased to properly enforce hard constraints.

## Genetic Algorithm Components

### Initialization
- **Random initialization:** Generate random timeslot assignments
- **Greedy initialization (25% of population):** Use a constructive heuristic that assigns exams to slots minimizing conflicts with already-scheduled exams

### Selection
- **Tournament selection** (k=5): Randomly select 5 individuals and choose the best

### Crossover
- **Uniform crossover** (probability=0.8): Each gene has 50% chance to come from either parent
- Alternative: One-point crossover (implemented but not used by default)

### Mutation
- **Basic mutation** (probability=0.1): Randomly reassign timeslots
- Alternatives implemented: swap, creep, adaptive, smart (implemented but not actively used)

### Elitism
- Top 5% of population is preserved across generations

## Project Structure

```
├── genetic_algo.py      # Main GA implementation
├── fitnesses.py         # Fitness function
├── crossovers.py        # Crossover operators
├── mutations.py         # Mutation operators
├── data_utils.py        # Data loading utilities
├── statistics.py        # Result statistics and reporting
├── correctedIIc/        # Dataset directory
│   └── ear-f-83-3.stu  # Student exam data
└── README.md           # This file
```

## How to Run

### Requirements
- Python 3.7+
- No external dependencies required (uses only standard library)

### Basic Run
```bash
python genetic_algo.py
```

This will run a single GA with default parameters:
- Population size: 150
- Generations: 50
- Crossover probability: 0.8
- Mutation probability: 0.1
- Tournament size: 5

### Running Experiments

To run multiple experiments with different configurations, uncomment the experiment section in `genetic_algo.py` (lines 236-251).

## Current Results

**Single run (50 generations, population=150):**
- Best penalty per student: ~25.61
- Same-slot conflicts: 193 ⚠️
- Total students with conflicts: 1100/1108

**Issues:**
- Hard constraints are not fully satisfied (193 same-slot conflicts remain)
- Need to increase penalty for same-slot conflicts or add repair mechanism

## Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `pop_size` | 150 | Population size |
| `max_generations` | 50 | Maximum number of generations |
| `crossover_prob` | 0.8 | Probability of crossover |
| `mutation_prob` | 0.1 | Probability of mutation per gene |
| `tournament_k` | 5 | Tournament size for selection |
| `elite_size` | 5% of pop | Number of elites preserved |
| `time_slots` | 30 | Number of available timeslots |

## Future Improvements

1. **Fix hard constraints:** Increase penalty for same-slot conflicts or add repair operator
2. **Experimental comparison:** Test different parameter settings systematically
3. **Advanced operators:** Implement and test problem-specific crossover/mutation
4. **Visualization:** Add convergence plots and schedule visualizations
5. **Multiple datasets:** Test on other Toronto benchmark instances

## References

- Carter, M. W., Laporte, G., & Lee, S. Y. (1996). Examination timetabling: Algorithmic strategies and applications. Journal of the Operational Research Society, 47(3), 373-383.
- Toronto Benchmark Datasets: https://www.cs.nott.ac.uk/~pszrq/data.htm