from random import randint
class Person:
    actual_year = 2022

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def birth_year(self):
        return self.actual_year-self.age
    
    @classmethod 
    def birth_year(cls,name,birth_year):
        idade = cls.actual_year-birth_year
        return cls(name,birth_year)

#To define a method utilize a @
#it isn't related to the instanse, but to the class itself
#cls it's a convention utilizated to refer to the class 

    @staticmethod
    def make_id():
        return randint(1000,1999)

#The static method dosn't need any instance or class


p1 = Person.birth_year('Name',2003)
print(p1)
print(p1.name,p1.age)
print(p1.make_id())