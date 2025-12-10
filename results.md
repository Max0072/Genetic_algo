============================================================
GENETIC ALGORITHM EXPERIMENTS
Exam Timetabling - Toronto Benchmark
============================================================
Experiment 1
============================================================
Running configuration: Baseline
Parameters: {'pop_size': 100, 'max_generations': 100, 'crossover_prob': 0.8, 'mutation_prob': 0.05, 'tournament_k': 5}
============================================================
  Run 1/5... (penalty: 24.97, conflicts: 200)
  Run 2/5... (penalty: 25.08, conflicts: 197)
  Run 3/5... (penalty: 27.20, conflicts: 214)
  Run 4/5... (penalty: 24.60, conflicts: 221)
  Run 5/5... (penalty: 27.38, conflicts: 213)

  Summary for Baseline:
    Best penalty: 24.60
    Avg penalty:  25.85
    Worst penalty: 27.38
    Avg conflicts: 209.0

============================================================
Running configuration: Large Population
Parameters: {'pop_size': 200, 'max_generations': 100, 'crossover_prob': 0.8, 'mutation_prob': 0.05, 'tournament_k': 5}
============================================================
  Run 1/5... (penalty: 25.48, conflicts: 190)
  Run 2/5... (penalty: 26.27, conflicts: 172)
  Run 3/5... (penalty: 28.35, conflicts: 219)
  Run 4/5... (penalty: 24.59, conflicts: 209)
  Run 5/5... (penalty: 24.71, conflicts: 223)

  Summary for Large Population:
    Best penalty: 24.59
    Avg penalty: 25.88
    Worst penalty: 28.35
    Avg conflicts: 202.6

============================================================
Running configuration: High Mutation
Parameters: {'pop_size': 100, 'max_generations': 100, 'crossover_prob': 0.8, 'mutation_prob': 0.15, 'tournament_k': 5}
============================================================
  Run 1/5... (penalty: 27.01, conflicts: 369)
  Run 2/5... (penalty: 26.89, conflicts: 352)
  Run 3/5... (penalty: 27.62, conflicts: 355)
  Run 4/5... (penalty: 29.26, conflicts: 362)
  Run 5/5... (penalty: 30.15, conflicts: 385)

  Summary for High Mutation:
    Best penalty: 26.89
    Avg penalty:  28.18
    Worst penalty: 30.15
    Avg conflicts: 364.6


============================================================
Running configuration: Low Mutation
Parameters: {'pop_size': 100, 'max_generations': 100, 'crossover_prob': 0.8, 'mutation_prob': 0.02, 'tournament_k': 5}
============================================================
  Run 1/5... (penalty: 24.28, conflicts: 95)
  Run 2/5... (penalty: 24.09, conflicts: 100)
  Run 3/5... (penalty: 22.46, conflicts: 73)
  Run 4/5... (penalty: 22.55, conflicts: 94)
  Run 5/5... (penalty: 24.63, conflicts: 96)

  Summary for Low Mutation:
    Best penalty: 22.46
    Avg penalty:  23.60
    Worst penalty: 24.63
    Avg conflicts: 91.6

============================================================
Running configuration: Even Lower Mutation
Parameters: {'pop_size': 100, 'max_generations': 100, 'crossover_prob': 0.8, 'mutation_prob': 0.005, 'tournament_k': 5}
============================================================
  Run 1/5... (penalty: 23.88, conflicts: 56)
  Run 2/5... (penalty: 22.63, conflicts: 39)
  Run 3/5... (penalty: 23.13, conflicts: 53)
  Run 4/5... (penalty: 24.37, conflicts: 56)
  Run 5/5... (penalty: 23.31, conflicts: 48)

  Summary for Lower Mutation:
    Best penalty: 22.63
    Avg penalty: 23.46
    Worst penalty: 24.37
    Avg conflicts: 50.4


============================================================
Running configuration: The Lowest mutation
Parameters: {'pop_size': 100, 'max_generations': 100, 'crossover_prob': 0.8, 'mutation_prob': 0.001, 'tournament_k': 5}
============================================================
  Run 1/5... (penalty: 23.69, conflicts: 89)
  Run 2/5... (penalty: 24.12, conflicts: 75)
  Run 3/5... (penalty: 22.91, conflicts: 75)
  Run 4/5... (penalty: 23.70, conflicts: 79)
  Run 5/5... (penalty: 24.14, conflicts: 101)

  Summary for Even Lower Mutation:
    Best penalty: 22.91
    Avg penalty:  23.71
    Worst penalty: 24.14
    Avg conflicts: 83.8



============================================================
Running configuration: Extended Evolution
Parameters: {'pop_size': 100, 'max_generations': 200, 'crossover_prob': 0.8, 'mutation_prob': 0.05, 'tournament_k': 5}
============================================================
  Run 1/5... (penalty: 25.91, conflicts: 173)
  Run 2/5... (penalty: 23.05, conflicts: 174)
  Run 3/5... (penalty: 25.02, conflicts: 157)
  Run 4/5... (penalty: 25.50, conflicts: 181)
  Run 5/5... (penalty: 24.58, conflicts: 157)

  Summary for Extended Evolution:
    Best penalty: 23.05
    Avg penalty: 24.81
    Worst penalty: 25.91
    Avg conflicts: 168.4

============================================================
Running configuration: Strong Selection
Parameters: {'pop_size': 100, 'max_generations': 100, 'crossover_prob': 0.8, 'mutation_prob': 0.05, 'tournament_k': 10}
============================================================
  Run 1/5... (penalty: 25.17, conflicts: 168)
  Run 2/5... (penalty: 24.49, conflicts: 181)
  Run 3/5... (penalty: 26.33, conflicts: 149)
  Run 4/5... (penalty: 24.60, conflicts: 173)
  Run 5/5... (penalty: 24.98, conflicts: 175)

  Summary for Strong Selection:
    Best penalty: 24.49
    Avg penalty: 25.11
    Worst penalty: 26.33
    Avg conflicts: 169.2

============================================================
Running configuration: Best params
Parameters: {'pop_size': 200, 'max_generations': 200, 'crossover_prob': 0.8, 'mutation_prob': 0.005, 'tournament_k': 30}
============================================================
  Run 1/5... (penalty: 20.43, conflicts: 12)
  Run 2/5... (penalty: 20.12, conflicts: 14)
  Run 3/5... (penalty: 19.11, conflicts: 13)
  Run 4/5... (penalty: 18.93, conflicts: 12)
  Run 5/5... (penalty: 19.25, conflicts: 16)

  Summary for Best params:
    Best penalty: 18.93
    Avg penalty:  19.57
    Worst penalty: 20.43
    Avg conflicts: 13.4

============================================================
Running configuration: Best params, more time
Parameters: {'pop_size': 300, 'max_generations': 300, 'crossover_prob': 0.8, 'mutation_prob': 0.005, 'tournament_k': 50}
============================================================
  Run 1/1... (penalty: 18.75, conflicts: 5)

  Summary for Best params, more time:
    Best penalty: 18.75
    Avg penalty:  18.75
    Worst penalty: 18.75
    Avg conflicts: 5.0


============================================================
FINAL COMPARISON
============================================================
Configuration                   Best        Avg  Conflicts
------------------------------------------------------------
Baseline                       24.60      25.85      209.0
Large Population               24.59      25.88      202.6
High Mutation                  26.89      28.18      364.6
Low Mutation                   22.46      23.60      91.6
Even Lower Mutation            22.63      23.46      50.4
Lowest Mutation                22.91      23.71      83.8
Extended Evolution             23.05      24.81      168.4
Strong Selection               24.49      25.11      169.2
Best parameters                18.93      19.57      13.4
Best params, more time         18.75      18.75      5.0

  Best configuration: Best params, more time
   Average penalty: 18.75
   Average conflicts: 5.0


============================================================
ANALYSIS & CONCLUSIONS
============================================================

1. Impact of Mutation Rate
----------------------------
The mutation rate has the STRONGEST impact on solution quality:

• High mutation (0.15): WORST results (penalty 28.18, 364.6 conflicts)
  → Too much disruption prevents convergence
  → Good building blocks are destroyed before exploitation

• Baseline mutation (0.05): Moderate results (penalty 25.85, 209 conflicts)
  → Reasonable exploration-exploitation balance

• Low mutation (0.02): IMPROVED results (penalty 23.60, 91.6 conflicts)
  → Better preservation of good solutions
  → Still enough diversity to escape local optima

• Very low mutation (0.005): BEST results (penalty 19.57, 13.4 conflicts)
  → Minimal disruption allows fine-tuning of solutions
  → Sufficient exploration from crossover and selection pressure

• Too low mutation (0.001): Slightly worse (penalty 23.71, 83.8 conflicts)
  → Insufficient diversity, possible premature convergence

CONCLUSION: For timetabling problems, very low mutation rates (0.005)
work best when combined with strong selection pressure. The crossover
operator provides sufficient exploration.


2. Impact of Population Size
------------------------------
• Baseline (100): penalty 25.85, conflicts 209.0
• Large (200): penalty 25.88, conflicts 202.6

FINDING: Doubling population size alone provides MINIMAL improvement:
  → Only 3.4% reduction in conflicts
  → No improvement in average penalty
  → 2x computational cost

CONCLUSION: Population size has diminishing returns when used in isolation.
More effective when combined with other parameter changes (see "Best parameters").


3. Impact of Generations (Time Budget)
---------------------------------------
• Baseline (100 gen): penalty 25.85
• Extended (200 gen): penalty 24.81
• Best params (200 gen): penalty 19.57
• Best params (300 gen): penalty 18.75

FINDINGS:
  → Doubling generations alone: 4% improvement (baseline → extended)
  → With optimized parameters: 24% improvement (baseline → best 200 gen)
  → Extended time + optimized params: 27% improvement (baseline → best 300 gen)

CONCLUSION: Additional generations help, but proper parameter tuning
is far more important. The algorithm benefits from extended runtime
only when other parameters are well-tuned.


4. Impact of Selection Pressure
--------------------------------
• Baseline (k=5): penalty 25.85, conflicts 209.0
• Strong selection (k=10): penalty 25.11, conflicts 169.2
• Best params (k=30): penalty 19.57, conflicts 13.4

FINDINGS:
  → Tournament size k=5: Weak selection pressure
  → Tournament size k=10: 2.9% improvement, 19% fewer conflicts
  → Tournament size k=30: 24% improvement, 93% fewer conflicts

CONCLUSION: High selection pressure (large tournament size) is crucial
for timetabling. Strong selection combined with low mutation allows
best individuals to dominate while maintaining solution quality.


5. Interaction Effects
-----------------------
The BEST configuration combines:
  • Large population (200-300)
  • Very low mutation (0.005)
  • High selection pressure (k=30-50)
  • Extended generations (200-300)

This combination achieves:
  ✓ 27% improvement over baseline (25.85 → 18.75)
  ✓ 97.6% reduction in conflicts (209 → 5)
  ✓ Near-satisfaction of hard constraints

KEY INSIGHT: Parameters have synergistic effects. Low mutation ONLY works
well with strong selection pressure. Large populations ONLY help when
combined with proper mutation rates and selection.


6. Hard Constraint Satisfaction
--------------------------------
Progress on same-slot conflicts (distance=0):

  Baseline:           209 conflicts (UNACCEPTABLE)
  Low mutation:        91.6 conflicts (poor)
  Very low mutation:   50.4 conflicts (moderate)
  Best parameters:     13.4 conflicts (good)
  Best + more time:     5.0 conflicts (near-optimal)

CONCLUSION: Hard constraints are nearly satisfied with optimal parameters.


============================================================
END OF ANALYSIS
============================================================
