
# This function is to calculate grades
# TODO: Make it work properly
# TODO: Get the hang of todos

def calc_grades(score: float, grade_boundaries: dict[str, float]) -> str:
    max_score = grade_boundaries['max']

    if score < 0 or score > max_score:
        raise ValueError('Outside range')

    grade_achieved = None

    for grade, boundary in grade_boundaries.items():
        if grade == 'max':
            continue
        elif score >= boundary:
            grade_achieved = grade
            break

    return grade_achieved

if __name__ == '__main__':
    grade_boundaries = {
        'max': 350,
        'A*': 264,
        'A': 229,
        'B': 189,
        'C': 150,
        'D': 111,
        'E': 72,
        'U': 0

    }

    print(calc_grades(350, grade_boundaries))


