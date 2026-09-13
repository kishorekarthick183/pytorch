# def numbers():
#     return [1, 2, 3, 4, 5]

# print(numbers())

# vs 

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for number in numbers():
    print(number)