import random


def boo(n1, n2, n3):
    """boo (n1, n2, n3) - returns the middle value when n1, n2, and n3 are sorted from lowest to highest"""
    list = [n1, n2, n3]
    list.sort()
    return list[1]


for x in range(10):
    n1 = random.randint(1, 1000000)
    n2 = random.randint(1, 1000000)
    n3 = random.randint(1, 1000000)

    n = boo(n1, n2, n3)

    print("\nNumbers in: {}, {}, {}".format(n1, n2, n3))
    print("Number returned: {}".format(n))
