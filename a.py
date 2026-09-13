class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

s1 = Student("Kishore", 22)
s2 = Student("Arun", 21)

s1.introduce()
s2.introduce()