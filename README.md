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

## Chromosome Encoding

**Representation:** Direct encoding as a list of integers
- Length: 189 (number of exams)
- Each index represents an exam (0-indexed)
- Each value represents the assigned timeslot (0-29)

Example: `[5, 12, 3, ...]` means:
- Exam 0 → Timeslot 5
- Exam 1 → Timeslot 12
- Exam 2 → Timeslot 3


## Fitness Function

The fitness function minimizes the total penalty across all students:

```
fitness = -1 * (total_penalty / num_students)
```

Where `total_penalty` is calculated by:
1. For each student, check all pairs of their exams
2. Calculate distance between timeslots
3. Apply penalty based on distance (10000 for same-slot, 8 for adjacent)

Total penalty in the final stats is calculated with the fine value of 16 for the same slot

## How to Run

### Basic Run

`genetic_algo.py` will run a single GA with default parameters

### Running Experiments

To run multiple experiments with different configurations: `run_experiment.py`

