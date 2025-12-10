"""
Experiment runner for comparing different GA configurations.

This script runs multiple GA configurations, each repeated several times,
and reports the results to compare performance.
"""

import json
from genetic_algo import genetic_algorithm
from data_utils import read_exam_data

def run_experiment_config(config_name, runs=5, **ga_params):
    print(f"\n{'='*60}")
    print(f"Running configuration: {config_name}")
    print(f"Parameters: {ga_params}")
    print(f"{'='*60}")

    results = []
    best_fitnesses = []
    avg_penalties = []
    num_conflicts = []

    for run in range(runs):
        print(f"  Run {run+1}/{runs}...", end=" ", flush=True)

        best_sol, best_fit, final_gen = genetic_algorithm(
            verbose=False,
            **ga_params
        )

        # Calculate detailed stats
        from statistics import get_genome_statistics
        student_exams, _ = read_exam_data('./correctedIIc/ear-f-83-3.stu')
        stats = get_genome_statistics(best_sol, student_exams, 30)

        results.append({
            'run': run + 1,
            'best_fitness': best_fit,
            'final_generation': final_gen,
            'avg_penalty': stats['avg_penalty_per_student'],
            'conflicts': stats['num_conflicts'],
            'slots_used': stats['num_used_slots']
        })

        best_fitnesses.append(best_fit)
        avg_penalties.append(stats['avg_penalty_per_student'])
        num_conflicts.append(stats['num_conflicts'])

        print(f"(penalty: {stats['avg_penalty_per_student']:.2f}, conflicts: {stats['num_conflicts']})")

    # Calculate summary statistics
    summary = {
        'config_name': config_name,
        'parameters': ga_params,
        'runs': runs,
        'best_fitness': {
            'best': max(best_fitnesses),
            'worst': min(best_fitnesses),
            'avg': sum(best_fitnesses) / len(best_fitnesses),
        },
        'avg_penalty': {
            'best': min(avg_penalties),
            'worst': max(avg_penalties),
            'avg': sum(avg_penalties) / len(avg_penalties),
        },
        'conflicts': {
            'best': min(num_conflicts),
            'worst': max(num_conflicts),
            'avg': sum(num_conflicts) / len(num_conflicts),
        },
        'detailed_runs': results
    }

    # Print summary
    print(f"\n  Summary for {config_name}:")
    print(f"    Best penalty: {summary['avg_penalty']['best']:.2f}")
    print(f"    Avg penalty:  {summary['avg_penalty']['avg']:.2f}")
    print(f"    Worst penalty: {summary['avg_penalty']['worst']:.2f}")
    print(f"    Avg conflicts: {summary['conflicts']['avg']:.1f}")

    return summary


def main():
    """Run all experiment configurations."""

    print("="*60)
    print("GENETIC ALGORITHM EXPERIMENTS")
    print("Exam Timetabling - Toronto Benchmark")
    print("="*60)

    all_results = []

    # Configuration 1: Baseline
    config1 = run_experiment_config(
        config_name="Baseline",
        runs=5,
        pop_size=100,
        max_generations=100,
        crossover_prob=0.8,
        mutation_prob=0.05,
        tournament_k=5
    )
    all_results.append(config1)

    # Configuration 2: Larger population
    config2 = run_experiment_config(
        config_name="Large Population",
        runs=5,
        pop_size=200,
        max_generations=100,
        crossover_prob=0.8,
        mutation_prob=0.05,
        tournament_k=5
    )
    all_results.append(config2)

    # Configuration 3: Higher mutation
    config3 = run_experiment_config(
        config_name="High Mutation",
        runs=5,
        pop_size=100,
        max_generations=100,
        crossover_prob=0.8,
        mutation_prob=0.15,
        tournament_k=5
    )
    all_results.append(config3)

    # Configuration 4: More generations
    config4 = run_experiment_config(
        config_name="Extended Evolution",
        runs=5,
        pop_size=100,
        max_generations=200,
        crossover_prob=0.8,
        mutation_prob=0.05,
        tournament_k=5
    )
    all_results.append(config4)

    # Configuration 5: Stronger selection pressure
    config5 = run_experiment_config(
        config_name="Strong Selection",
        runs=5,
        pop_size=100,
        max_generations=100,
        crossover_prob=0.8,
        mutation_prob=0.05,
        tournament_k=10
    )
    all_results.append(config5)

    # Print comparison table
    print("\n" + "="*60)
    print("FINAL COMPARISON")
    print("="*60)
    print(f"{'Configuration':<25} {'Best':>10} {'Avg':>10} {'Conflicts':>10}")
    print("-"*60)

    for result in all_results:
        name = result['config_name']
        best = result['avg_penalty']['best']
        avg = result['avg_penalty']['avg']
        conflicts = result['conflicts']['avg']
        print(f"{name:<25} {best:>10.2f} {avg:>10.2f} {conflicts:>10.1f}")

    # Find best configuration
    best_config = min(all_results, key=lambda x: x['avg_penalty']['avg'])
    print(f"\n  Best configuration: {best_config['config_name']}")
    print(f"   Average penalty: {best_config['avg_penalty']['avg']:.2f}")
    print(f"   Average conflicts: {best_config['conflicts']['avg']:.1f}")

    # Save results to JSON
    with open('experiment_results.json', 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"\n Results saved to experiment_results.json")

    return all_results


if __name__ == "__main__":
    main()