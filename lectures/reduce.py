#reduce = уменьшить


numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num

print (result)

def reduce(func, iterable, initial):
    result = initial
    for i in iterable:
        result = func(result, i)
    return result

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers, 0)
print(result)
