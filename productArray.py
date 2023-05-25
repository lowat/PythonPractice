def arrayOfProducts(array):
    result = []
    leftProducts(array, result)
    rightProducts(array, result)
    return result

def leftProducts(array, result):
    product = 1
    for i in range(len(array)):
        result.append(product)
        product *= array[i]

def rightProducts(array, result):
    product = 1
    for i in reversed(range(len(array))):
        result[i] *= product
        product *= array[i]