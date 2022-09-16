class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        #I Can creat a variable without the "self."" but it will be only valid insid of the "init" method

    def say_hello(self):
        print(f"Hello my name is {self.name}, my age is {self.age} and my weight {self.weight}")

name = input("Input your name: ")
age = int(input("Input your age: "))
weight = float(input("Input your weight: "))
test = Person(name,age,weight)
test.say_hello()