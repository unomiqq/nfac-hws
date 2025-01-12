#My_List = [3, 5, 7, 9]
import copy

a = [1, 2, 3, 4]
"""
a.extend([1, 3])
print(a)
# [1, 2, 3, 4, 1, 3]
a.append([5, 6])
print(a)
# [1, 2, 3, 4, 1, 3, [5, 6]]
"""
"""
b = a
print(a is b)
#True
b.append(5)
print(a, b)
#[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
a[1] = 99
print(a)
"""

b = a[:]
#copy list a. you can change b without change a
b = copy.deepcopy(a)
# copy list of lists
a.sort()
# sort list a
a.reverse()
#reverse
