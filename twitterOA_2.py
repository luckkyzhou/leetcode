
def balancedSum(sales):

    for i in range(len(sales)):
        sumLeft = sum(sales[:i])
        sumRight = sum(sales[i + 1:])
        if sumLeft == sumRight:
            return i