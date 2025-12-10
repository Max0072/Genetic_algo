from typing import List


# ------ fitness function --------------------------------------
def fitness(genome: List[int], student_exams) -> float:
    total_penalty = 0
    total_students = len(student_exams)

    for student, exams in student_exams.items():
        time_slots = [genome[exam - 1] for exam in exams]

        for i in range(len(exams)):
            for j in range(i + 1, len(exams)):
                distance = abs(time_slots[i] - time_slots[j])

                if distance == 0:
                    total_penalty += 10000
                elif distance == 1:
                    total_penalty += 8
                elif distance == 2:
                    total_penalty += 4
                elif distance == 3:
                    total_penalty += 2
                elif distance == 4:
                    total_penalty += 1

    return -1 * (total_penalty / total_students)