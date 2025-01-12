a = [1, 99, 3, 5]
for i in a:
    print(i)

for i, j in enumerate(a):
    print(f'i:{i}, j:{j}')

print(a[::2])
#every 2nd el of list
print(a[:1])
#starting with 1st el
print(a[0:3])
#until 3rd el
