g_10 = 10
def say():
    global g_10
    print(g_10)
    g_10 = 90

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
