# 3
li = ['Claus', 'Ib', 'Per']
print(sorted(li))
print(sorted(li, reverse=True))
print(sorted(li, key=len))


def last_lettter(x):
    return x[-1][-1]


print(sorted(li, key=last_lettter))

# Sort the list with the names where the letter ‘a’ is in the name first.


def aNameFirst(x):
    if 'a' in x:
        return 0
    else:
        return 1


print(sorted(li, key=aNameFirst))
