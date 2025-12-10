from typing import List, Tuple
import random


# ------- Crossover -------------------------------------------------------------------- done
def uniform_crossover(parent1: List[int], parent2: List[int],
                      mix_ratio: float = 0.5, crossover_prob: float = 0.8) -> Tuple[List[int], List[int]]:
    n = len(parent1)
    assert len(parent2) == n
    if random.random() >= crossover_prob:
        return parent1, parent2

    child1, child2 = [], []
    for i in range(n):
        if random.random() < mix_ratio:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1, child2


# ------- Crossover -------------------------------------------------------------------- done
def one_point_crossover(parent1: List[int], parent2: List[int],
                        crossover_prob: float = 0.8) -> Tuple[List[int], List[int]]:
    n = len(parent1)
    assert len(parent2) == n

    if random.random() >= crossover_prob:
        return parent1, parent2
    else:
        c = random.randint(1, n-1)
        child1 = parent1[0:c] + parent2[c:n]
        child2 = parent2[0:c] + parent1[c:n]
        return child1, child2


# ------- Crossover -------------------------------------------------------------------- done
def multi_point_crossover(parent1: List[int], parent2: List[int],
                          n_points: int = 3, crossover_prob: float = 0.8) -> Tuple[List[int], List[int]]:

    n = len(parent1)
    assert len(parent2) == n
    assert 1 <= n_points < n

    if random.random() >= crossover_prob:
        return parent1, parent2

    points = sorted(random.sample(range(1, n), n_points)) + [n]

    child1, child2 = [], []
    prev_point = 0
    from_parent1 = True
    for point in points:
        if from_parent1:
            child1.extend(parent1[prev_point:point])
            child2.extend(parent2[prev_point:point])
        else:
            child1.extend(parent2[prev_point:point])
            child2.extend(parent1[prev_point:point])
        prev_point = point
        from_parent1 = not from_parent1

    return child1, child2
