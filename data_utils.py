from typing import Dict, List, Tuple

# ------ Reading exam data -------------------------
def read_exam_data(file_path: str) -> Tuple[Dict[int, List[int]], int]:
    student_exams: Dict[int, List[int]] = {}
    max_exam_id = 0

    with open(file_path, 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
            line = line.strip()
            if not line:
                continue

            student_id = line_count
            exams = list(map(int, line.split()))

            student_exams[student_id] = exams

            if exams:
                max_exam_id = max(max_exam_id, max(exams))

    return student_exams, max_exam_id