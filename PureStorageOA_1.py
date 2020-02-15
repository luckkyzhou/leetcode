def compute_number_score(number: int):
    sum = 0
    numberStr = str(number)

    for i in range(len(numberStr)):
        # Every 9 in number +4
        if numberStr[i] == '9': sum += 4
        # Each even digit +2
        if int(numberStr[i]) % 2 == 0: sum += 2

    sequence = 1
    for i in range(1, len(numberStr)):
        # Consecutive 1s +5
        if numberStr[i] == '1' and numberStr[i - 1] == '1': sum += 5
        # Sequence of length N +N^2
        if int(numberStr[i]) - int(numberStr[i - 1]) == 1: sequence += 1
        else:
            sum += sequence ** 2
            sequence = 1
    sum += sequence ** 2

    # Multiple of 7 +1
    if number % 7 == 0: sum += 1

    return sum