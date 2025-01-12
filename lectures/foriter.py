def find_adults(l):
    for i in l:
        if i >= 18:
            return i

ages = [10, 20, 3, 22, 4, 50, 99]
print(find_adults(ages))

ages_iter = iter(ages)
print(find_adults(ages_iter))
print(find_adults(ages_iter))
print(find_adults(ages_iter))
print(find_adults(ages_iter))
