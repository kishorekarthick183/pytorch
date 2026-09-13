class Student:
    credits = 3
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
print(s1.credits)
print(s2.credits)
# credits is class based not instance. both student have same credit