# что-то пошло не так, это неправильный Т-Т
import sys

num_of_grades = int(sys.stdin.read())
v_grades = sys.stdin.read()
v_grades = v_grades.replace(' ', '')
grades = []
for i in v_grades:
        try:
            grades.append(int(i))
        except ValueError:
            continue
        if len(grades) == num_of_grades:
            break

def count_presents(num_of_grades: int, grades: list) -> int:
    good_grades = []
    presents = 0
    for gr in grades:
        if gr == 4 or gr == 5:
            good_grades.append(gr)
            if len(good_grades) == 3:
                presents += 1
                good_grades = []
        else:
            good_grades = []
    return presents
