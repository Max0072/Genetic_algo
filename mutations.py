from typing import Tuple, List
import random


# ------ Mutation ---------------------------------------------------------------
def basic_mutate(genome: List[int], mutation_prob: float = 0.1,  time_slots=30) -> None:
    for i in range(len(genome)):
        if random.random() < mutation_prob:
            genome[i] = random.randint(0, time_slots - 1)

# ------ Mutation ---------------------------------------------------------------
def swap_mutate(individual, mutation_prob=0.1):
    for _ in range(int(len(individual) * mutation_prob)):
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

# ------ Mutation ---------------------------------------------------------------
def creep_mutate(individual, mutation_prob=0.1, time_slots=30):
    for i in range(len(individual)):
        if random.random() < mutation_prob:
            delta = random.choice([-1, 1])
            individual[i] = (individual[i] + delta) % time_slots

# ------ Mutation ---------------------------------------------------------------
def adaptive_mutate(individual, generation, max_gen, time_slots=30):
    prob = 0.3 * (1 - generation/max_gen) + 0.01
    for i in range(len(individual)):
        if random.random() < prob:
            individual[i] = random.randint(0, time_slots-1)




