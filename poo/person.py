from datetime import datetime

class Person:
    #I can creat a variable for the hole class 
    actual_year = int(datetime.strftime(datetime.now(),'%Y'))

    def __init__ (self, name, age, eating = False, speaking = False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def speak(self, theme):
        if self.eating:
            print(f"\n{self.name} can't speak while eating")
            return
        
        if self.speaking:
            print(f"\n{self.name} is already speaking")
            return
        
        print(f"\n{self.name} is speaking about {theme}")
        self.speaking = True

    def stop_speak(self,theme):
        if not self.speak:
            print(f"\n{self.name} is not speaking")
            return
        
        print(f"\n{self.name} stop speaking about {theme}")
        self.speaking = False

    def eat(self,food):
        if self.eating:
            print(f"\n{self.name} is already eating {food}")
            return       
        
        if self.speaking:
            print(f"\n{self.name} can't eat while speaking")
            return

        print(f"\n{self.name} is eating {food}")
        self.eating = True

    def stop_eating(self,food):
        if not self.eating:
            print(f"\n{self.name} is not eating")
            return

        print(f"\n{self.name} stop eating {food}")
        self.eating = False

    def birth_year(self):
        return self.actual_year-self.age
