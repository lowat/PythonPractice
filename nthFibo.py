def getNthFib(n):
    values = [0, 1]
    for i in range(2, n):
        temp = values[1]
        values[1] = values[0] + values[1]
        values[0] = temp
    return values[1] if n > 1 else values[0]