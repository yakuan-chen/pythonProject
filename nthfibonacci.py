def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n-2)

def getNthFib2(n, m = {1: 0, 2: 1}):
    if n in m:
        return m[n]
    else:
        m[n] = getNthFib2(n-1, m) + getNthFib2(n-2, m)
        return m[n]

def getNthFib3(n):
    lasttwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lasttwo[0] + lasttwo[1]
        lasttwo[0] = lasttwo[1]
        lasttwo[1] = nextFib
        counter += 1
    return lasttwo[1] if n > 1 else lasttwo[0]

