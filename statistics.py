from typing import Dict, List



# ------ Statistics function -------------------------------------------
def get_genome_statistics(genome: List[int], student_exams: Dict[int, List[int]], num_time_slots: int) -> Dict:
    total_penalty = 0
    total_students = len(student_exams)

    conflicts_by_distance = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    student_penalties = []

    for student, exams in student_exams.items():
        time_slots = [genome[exam - 1] for exam in exams]
        student_penalty = 0

        for i in range(len(exams)):
            for j in range(i + 1, len(exams)):
                distance = abs(time_slots[i] - time_slots[j])

                if distance == 0:
                    penalty = 16
                    conflicts_by_distance[0] += 1
                elif distance == 1:
                    penalty = 8
                    conflicts_by_distance[1] += 1
                elif distance == 2:
                    penalty = 4
                    conflicts_by_distance[2] += 1
                elif distance == 3:
                    penalty = 2
                    conflicts_by_distance[3] += 1
                elif distance == 4:
                    penalty = 1
                    conflicts_by_distance[4] += 1
                else:
                    penalty = 0

                student_penalty += penalty
                total_penalty += penalty

        student_penalties.append((student, student_penalty))

    slot_distribution = {}
    for slot in genome:
        slot_distribution[slot] = slot_distribution.get(slot, 0) + 1

    student_penalties.sort(key=lambda x: x[1], reverse=True)
    worst_students = student_penalties[:5]

    return {
        'total_penalty': total_penalty,
        'avg_penalty_per_student': total_penalty / total_students,
        'num_conflicts': conflicts_by_distance[0],  # same slot
        'num_adjacent': conflicts_by_distance[1],   # adjacent slots
        'num_distance_2': conflicts_by_distance[2],
        'num_distance_3': conflicts_by_distance[3],
        'num_distance_4': conflicts_by_distance[4],
        'num_used_slots': len(set(genome)),
        'slot_distribution': slot_distribution,
        'time_slots': num_time_slots,
        'worst_students': worst_students,
        'students_with_conflicts': sum(1 for _, p in student_penalties if p > 0)
    }

# ------ Print statistics --------------------------------------------------
def print_statistics(stats: Dict) -> None:

    print("\n" + "="*60)
    print("TIMETABLE STATISTICS")
    print("="*60)

    print(f"\n Overall Metrics:")
    print(f"  Total Penalty:              {stats['total_penalty']}")
    print(f"  Avg Penalty per Student:    {stats['avg_penalty_per_student']:.2f}")
    print(f"  Students with Conflicts:    {stats['students_with_conflicts']}")

    print(f"\n️ Conflict Breakdown:")
    print(f"  Same slot (distance=0):     {stats['num_conflicts']}")
    print(f"  Adjacent (distance=1):      {stats['num_adjacent']}")
    print(f"  Distance=2:                 {stats['num_distance_2']}")
    print(f"  Distance=3:                 {stats['num_distance_3']}")
    print(f"  Distance=4:                 {stats['num_distance_4']}")

    print(f"\n Slot Usage:")
    print(f"  Total slots used:           {stats['num_used_slots']}/{stats['time_slots']}")
    print(f"  Avg exams per slot:         {sum(stats['slot_distribution'].values()) / stats['num_used_slots']:.1f}")

    # Most loaded slots
    sorted_slots = sorted(stats['slot_distribution'].items(), key=lambda x: x[1], reverse=True)
    print(f"  Most loaded slots:")
    for slot, count in sorted_slots[:3]:
        print(f"    Slot {slot:2d}: {count} exams")

    print(f"\n Top 5 Worst Students:")
    for i, (student_id, penalty) in enumerate(stats['worst_students'], 1):
        print(f"  {i}. Student {student_id}: {penalty} penalty points")

    print("="*60)



