def getNthFib(n):
    prevValue = 1
    prevPrevValue = 0
    for i in range(2, n):
        temp = prevValue
        prevValue = prevValue + prevPrevValue
        prevPrevValue = temp
    return prevValue if n > 1 else prevPrevValue