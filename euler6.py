
def sumsquares(num):
    result = 0
    for i in range(num + 1):
        result = result + (i*i)
    return result


def squaresum(num):
    result = 0
    for i in range(num + 1):
        result = result + i
    return result * result

print(squaresum(100) - sumsquares(100))

