import random
from typing import List

# ------ Choose the best ----------------------------------------------------------------------------------
def tournament_selection(population: List[List[int]], fitnesses: List[int], k: int = 3) -> List[int]:
    indices = random.sample(range(len(population)), k) # 3 random indices
    chosen = [fitnesses[i] for i in indices] # 3 fitnesses
    return population[indices[chosen.index(max(chosen))]]