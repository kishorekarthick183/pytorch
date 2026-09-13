def logger(func):

    def wrapper():
        print("Function started")

        func()

        print("Function finished")

    return wrapper

@logger
def hello():
    print("Hello")

hello()