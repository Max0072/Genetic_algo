import random
from typing import List, Tuple, Dict

from statistics import get_genome_statistics, print_statistics

from data_utils import read_exam_data

from fitnesses import fitness
from crossovers import uniform_crossover
from mutations import basic_mutate, repair_conflicts


random.seed(42)

TIME_SLOTS = 30
NUM_EXAMS = 185



# ------ Single random sample init ---------------------------------- done
def random_genome(time_slots, exams) -> List[int]:
    """index is an exam number, the value is a time slot"""
    genome = [random.randint(0, time_slots-1) for _ in range(exams)]
    return genome

# ------ Multiple random samples init ---------------------------------------------
def create_initial_population(pop_size: int, time_slots: int, exams: int, student_exams: Dict = None) -> List[List[int]]:
    population: List[List[int]] = []

    # Fill rest with random
    for i in range(pop_size):
        population.append(random_genome(time_slots, exams))

    return population


# ------ Greedy initialization ---------------------------------------------
def greedy_genome(time_slots: int, exams: int, student_exams: Dict) -> List[int]:
    """Create a genome using greedy heuristic to minimize conflicts"""
    genome = [-1] * exams  # -1 means unassigned

    # Create exam conflict graph (which exams share students)
    exam_conflicts = {i: set() for i in range(1, exams + 1)}
    for student, student_exam_list in student_exams.items():
        for i in range(len(student_exam_list)):
            for j in range(i + 1, len(student_exam_list)):
                exam_conflicts[student_exam_list[i]].add(student_exam_list[j])
                exam_conflicts[student_exam_list[j]].add(student_exam_list[i])

    # Sort exams by number of conflicts (most constrained first)
    exam_order = sorted(range(1, exams + 1), key=lambda x: len(exam_conflicts[x]), reverse=True)

    for exam in exam_order:
        # Find slot with minimum conflicts
        slot_penalties = [0] * time_slots

        for slot in range(time_slots):
            for conflicting_exam in exam_conflicts[exam]:
                if genome[conflicting_exam - 1] != -1:
                    distance = abs(slot - genome[conflicting_exam - 1])
                    if distance == 0:
                        slot_penalties[slot] += 16
                    elif distance == 1:
                        slot_penalties[slot] += 8
                    elif distance == 2:
                        slot_penalties[slot] += 4
                    elif distance == 3:
                        slot_penalties[slot] += 2
                    elif distance == 4:
                        slot_penalties[slot] += 1

        # Assign to best slot (or random if all equal)
        best_penalty = min(slot_penalties)
        best_slots = [i for i, p in enumerate(slot_penalties) if p == best_penalty]
        genome[exam - 1] = random.choice(best_slots)

    return genome


# ------ Multiple random samples init ---------------------------------------------
def create_initial_population_greedy(pop_size: int, time_slots: int, exams: int, student_exams: Dict = None) -> List[List[int]]:
    population: List[List[int]] = []

    # Create some greedy individuals if student_exams is provided
    if student_exams:
        num_greedy = min(pop_size // 4, 10)  # 25% or max 10 greedy individuals
        for i in range(num_greedy):
            population.append(greedy_genome(time_slots, exams, student_exams))

    # Fill rest with random
    for i in range(len(population), pop_size):
        population.append(random_genome(time_slots, exams))

    return population



# ------ Choose the best ----------------------------------------------------------------------------------
def tournament_selection(population: List[List[int]], fitnesses: List[int], k: int = 3) -> List[int]:
    indices = random.sample(range(len(population)), k) # 3 random indices
    chosen = [fitnesses[i] for i in indices] # 3 fitnesses
    return population[indices[chosen.index(max(chosen))]]




# ------ Full algorithm -------------------------------------------------
def genetic_algorithm(pop_size: int = 50,
                      max_generations: int = 200,
                      crossover_prob: float = 0.8,
                      mutation_prob: float = 0.05,
                      tournament_k: int = 5,
                      time_slots: int = TIME_SLOTS,
                      elitism: bool = True,
                      elite_size: int = None,
                      verbose: bool = True):

    student_exams, max_exam_id = read_exam_data('./correctedIIc/ear-f-83-3.stu')
    num_exams = max_exam_id

    # Calculate elite size (default: 5% of population, min 1)
    if elite_size is None:
        elite_size = max(1, int(pop_size * 0.05))

    if verbose:
        print(f"Loaded {len(student_exams)} students, {max_exam_id} exams")
        print(f"Population: {pop_size}, Generations: {max_generations}")
        if elitism:
            print(f"Elitism: ON (elite_size={elite_size})")
        else:
            print(f"Elitism: OFF")


    # Init population
    population = create_initial_population(pop_size, time_slots, num_exams, student_exams)

    best_individual = None
    best_fitness = float("-inf")
    gen = 0

    # Main evolution loop
    for gen in range(max_generations):

        # 1. Evaluate fitness
        fitnesses = [fitness(ind, student_exams) for ind in population]

        # 2. Track best solution
        best_id = fitnesses.index(max(fitnesses))
        if fitnesses[best_id] > best_fitness:
            best_individual = population[best_id].copy()
            best_fitness = fitnesses[best_id]

        if verbose and gen % 10 == 0:
            print(f"Gen {gen}: Best fitness = {best_fitness:.4f}")

        # 3. Check for perfect solution (penalty = 0)
        if best_fitness == 0:
            if verbose:
                print(f"Perfect solution found at generation {gen}!")
            break

        # 4. Elitism - save best individuals
        elites = []
        if elitism and elite_size > 0:
            # Get indices of best individuals
            elite_indices = sorted(range(len(population)), key=lambda i: fitnesses[i], reverse=True)[:elite_size]
            elites = [population[i].copy() for i in elite_indices]

        # 5. Create new population
        new_population: List[List[int]] = []


        while len(new_population) < pop_size - len(elites):
            # a) Selection
            parent1 = tournament_selection(population, fitnesses, tournament_k)
            parent2 = tournament_selection(population, fitnesses, tournament_k)

            # b) Crossover
            child1, child2 = uniform_crossover(parent1, parent2, crossover_prob)

            # c) Mutation
            basic_mutate(child1, mutation_prob, time_slots)
            basic_mutate(child2, mutation_prob, time_slots)

            new_population.extend([child1, child2])

        # Trim offspring to exact size needed
        new_population = new_population[:pop_size - len(elites)]

        # Add elites to new population
        new_population.extend(elites)

        population = new_population

    if verbose:
        print(f"\nFinal best fitness: {best_fitness:.4f}")

    return best_individual, best_fitness, gen



# ------ Many runs -----------------------------------------
def run_experiments(runs: int = 5, **ga_params):
    """
    Run the GA 'runs' times with the given parameters.
    Return a list of (best_fitness, success_generation) pairs.
    """

    results = []
    for i in range(runs):
        # print(f"\n=== Run {i+1} ===")
        best, best_f, gen_succ = genetic_algorithm(verbose=False, **ga_params)
        # print("Best fitness:", best_f, "| success gen:", gen_succ)
        results.append((best_f, gen_succ))
    return results


if __name__ == "__main__":
    print("="*60)
    print("Genetic Algorithm for Exam Timetabling")
    print("="*60)

    # Load data for statistics
    student_exams, _ = read_exam_data('./correctedIIc/ear-f-83-3.stu')

    # Single run with verbose output
    print("\n--- Single Run Test ---")
    best_solution, best_fit, final_gen = genetic_algorithm(
        pop_size=150,
        max_generations=150,
        crossover_prob=0.8,
        mutation_prob=0.02,
        tournament_k=10,
        verbose=True
    )

    print(f"\nCompleted at generation: {final_gen}")
    print(f"Best penalty per student: {abs(best_fit):.4f}")

    # Show detailed statistics
    stats = get_genome_statistics(best_solution, student_exams, TIME_SLOTS)
    print_statistics(stats)
    # Multiple runs for statistics (commented out for now)
    # print("\n" + "="*60)
    # print("--- Running 10 experiments ---")
    # results = run_experiments(
    #     runs=10,
    #     pop_size=100,
    #     max_generations=500,
    #     crossover_prob=0.8,
    #     mutation_prob=0.05,
    #     tournament_k=5
    # )
    #
    # fitness_values = [f for f, _ in results]
    # print(f"\nBest fitness across all runs: {max(fitness_values):.4f}")
    # print(f"Average fitness: {sum(fitness_values)/len(fitness_values):.4f}")
    # print(f"Worst fitness: {min(fitness_values):.4f}")


