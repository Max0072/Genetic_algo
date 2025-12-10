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
