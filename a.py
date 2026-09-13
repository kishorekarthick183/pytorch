class MyContext:

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
    
with MyContext():
    print("Inside")

"""
obj = MyContext()

obj.__enter__()

try:
    print("Inside")
finally:
    obj.__exit__(...)
"""