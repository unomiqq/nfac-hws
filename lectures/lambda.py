"""sum = lambda x, y: x + y
res = sum(5, 10)
print(res)

numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))
#map - отобразить
"""

def map(func, iterable):
    result = []
    for i in iterable:
        result.append(func(i))
    return result

def process(num):
    squared = num ** 2
    subtracted = squared - 10
    return subtracted

print(map(process,[1, 2, 3, 4, 5]))
