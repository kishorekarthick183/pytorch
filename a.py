file = open("data.txt")
try:
    print(file.read())
finally:
    file.close()
