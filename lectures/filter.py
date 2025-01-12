def filter(func, iterable):
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result

def greater_than_five(num):
    return num > 5

numbers = [2, 7, 1, 8, 4, 5]
result = filter(greater_than_five, numbers)
print(result)
result = filter(lambda x: x > 5, numbers)
print(result)
