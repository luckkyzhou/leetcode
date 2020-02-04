def arraySum (inputs, tests):
    # Write your code here
    # Do O(n^2) loop to store all posible sum to an array.
    sum = []
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            sum.append(inputs[i] + inputs[j])

    # Convert tests array into a hashmap to reduce searching process to O(1).
    testsDict = set()
    for i in range(len(tests)):
        testsDict.add(tests[i])

    # Do a loop in sum array to check whether there is an answer.
    for i in range(len(sum)):
        if sum[i] in tests: return True
    return False