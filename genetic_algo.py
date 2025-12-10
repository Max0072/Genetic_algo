import random
from typing import List, Tuple, Dict

from statistics import get_genome_statistics, print_statistics

from data_utils import read_exam_data

from population_init import create_initial_population
from fitnesses import fitness
from selection import tournament_selection
from crossovers import uniform_crossover
from mutations import basic_mutate


random.seed(42)

TIME_SLOTS = 30
NUM_EXAMS = 185


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

    if elite_size is None:
        elite_size = max(1, int(pop_size * 0.05))

    if verbose:
        print(f"Loaded {len(student_exams)} students, {max_exam_id} exams")
        print(f"Population: {pop_size}, Generations: {max_generations}")
        if elitism:
            print(f"Elitism: ON (elite_size={elite_size})")
        else:
            print(f"Elitism: OFF")


    # Initialize population
    population = create_initial_population(pop_size, time_slots, num_exams)

    best_individual = None
    best_fitness = float("-inf")
    gen = 0

    # Evolution loop
    for gen in range(max_generations):

        # 1. Evaluate fitness
        fitnesses = [fitness(ind, student_exams) for ind in population]

        # 2. Check for best solution
        best_id = fitnesses.index(max(fitnesses))
        if fitnesses[best_id] > best_fitness:
            best_individual = population[best_id].copy()
            best_fitness = fitnesses[best_id]

        if verbose and gen % 10 == 0:
            print(f"Gen: {gen}, Best fitness: {best_fitness}")

        # 3. Elitism - save best individuals
        elites = []
        if elitism and elite_size > 0:
            # Get indices of best individuals
            elite_indices = sorted(range(len(population)), key=lambda i: fitnesses[i], reverse=True)[:elite_size]
            elites = [population[i].copy() for i in elite_indices]

        # 4. Create new population
        new_population: List[List[int]] = []


        while len(new_population) < pop_size - len(elites):
            # a) Selection
            parent1 = tournament_selection(population, fitnesses, tournament_k)
            parent2 = tournament_selection(population, fitnesses, tournament_k)

            # b) Crossover
            child1, child2 = uniform_crossover(parent1, parent2, crossover_prob=crossover_prob)

            # c) Mutation
            basic_mutate(child1, mutation_prob, time_slots)
            basic_mutate(child2, mutation_prob, time_slots)

            new_population.extend([child1, child2])

        new_population = new_population[:pop_size - len(elites)]
        new_population.extend(elites)
        population = new_population

    if verbose:
        print(f"\nFinal best fitness: {best_fitness:.4f}")

    return best_individual, best_fitness, gen



if __name__ == "__main__":
    print("="*60)
    print("Genetic Algorithm for Exam Timetabling")
    print("="*60)

    # Load data for statistics
    student_exams, _ = read_exam_data('./correctedIIc/ear-f-83-3.stu')

    # Single run with verbose output
    print("\n--- Single Run Test ---")
    best_solution, best_fit, final_gen = genetic_algorithm(
        pop_size=200,
        max_generations=200,
        crossover_prob=0.8,
        mutation_prob=0.005,
        tournament_k=30,
        verbose=True
    )

    print(f"\nCompleted at generation: {final_gen}")
    print(f"Best penalty per student: {abs(best_fit):.4f}")

    # Show detailed statistics
    stats = get_genome_statistics(best_solution, student_exams, TIME_SLOTS)
    print_statistics(stats)
