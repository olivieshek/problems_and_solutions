'''
хорошие: 4 и 5

1 подарок = 3 хороших оценки подряд
'''

vasya_grades = [4, 5, 5, 5, 5, 3, 4, 3, 5]
def count_presents(vasya_grades: list) -> int:
    good_grades = []
    presents = 0
    for gr in vasya_grades:
        if gr == 4 or gr == 5:
            good_grades.append(gr)
            if len(good_grades) == 3:
                presents += 1
                good_grades = []
            else:
                continue
        else:
            good_grades = []
    return presents

assert count_presents(vasya_grades) == 1