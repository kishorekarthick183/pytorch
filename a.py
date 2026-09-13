def logger(func):

    def wrapper():
        print("Function started")

        func()

        print("Function finished")

    return wrapper

def hello():
    print("Hello")

hello = logger(hello)

hello()