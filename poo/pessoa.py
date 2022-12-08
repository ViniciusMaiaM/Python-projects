from datetime import datetime

class Person:
    
    actual_year = int(datetime.strftime(datetime.now(),'%Y'))
    
    def __init__(self,name,date,height):
        self.name = name
        self.date = date
        self.height = height
    
    @property
    def date(self):
        self.new_date

    @date.setter
    def valid_date(self,year):
        year = self.date
        if isinstance(year,str):
            list(year)
            del year[0:5]
            year = int(year)
        self.new_date = year

    def calculate_age (self):
        return self.actual_year - self.new_date

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Birth date: {self.date}")
        print(f"Height: {self.height}")
        print(f"The person has {self.calculate_age()}")

print("Hi, to test our class let's input the following requests!")
name = input("Your name: ")
birthdate = input("Your birthdate: ")
height = input("Your heigh: ")

p1 = Person(name,birthdate,height)
