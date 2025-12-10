import random
from typing import List

# ------ Single random sample init ---------------------------------- done
def random_genome(time_slots, exams) -> List[int]:
    genome = [random.randint(0, time_slots-1) for _ in range(exams)]
    return genome

# ------ Multiple random samples init ------------------------------- done
def create_initial_population(pop_size: int, time_slots: int, exams: int) -> List[List[int]]:
    population: List[List[int]] = []
    for i in range(pop_size):
        population.append(random_genome(time_slots, exams))
    return population