def numbers():
    print("Before 1")
    yield 1

    print("Before 2")
    yield 2

    print("Before 3")
    yield 3

g = numbers()
print(g)
print(next(g))
print(next(g))