students_and_grades = {}

num = int(input())

for i in range(num):
    name , grade = input().split()
    if name not in students_and_grades:
        students_and_grades[name] = []
    students_and_grades[name].append(float(grade))

for name , grades in students_and_grades.items():
    avg_grade = sum(grades) / len(grades)
    grades_str = ' '.join([str(f'{g:.2f}') for g in grades])
    print(f"{name} -> {grades_str} (avg: {avg_grade:.2f})")
