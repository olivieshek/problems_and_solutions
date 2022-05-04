# Через for in range(разница значений)

def days_diff(a, b):
    diff = [0, 0, 0]
    result = [0, 0, 0]
    for i in range(len(a)):
        diff[i] = abs(a[i] - b[i])
    result[2] += diff[2]
    for m in range(diff[1]):
        if m == 2 and diff[0] % 4:
            result[1] += 28
        elif m == 2 and not diff[0] % 4:
            result[1] += 29
        elif m % 2:
            result[1] += 31
        else:
            result[1] += 30
    for i in range(a[0] + 1, b[0] + 1):
        if i % 4:
            result[0] += 365
        else:
            result[0] += 366
    return sum(result)


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1986, 6, 22)))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    # assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    # assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    # print("Coding complete? Click 'Check' to earn cool rewards!")