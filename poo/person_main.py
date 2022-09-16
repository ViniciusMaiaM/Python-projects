from person import Person
import os

os.system('clear')

print("\nHi, let's try some initial thing with OOP.")
name = input("\nAt first, input your name: ")
age = int(input("\nYour age: "))
theme = input("\nSomething that you like to talk about: ")
food = input("\nAnd something that you like to eat: ")

p1 = Person(name,age)

p1.speak(theme)
p1.stop_speak(theme)
p1.eat(food)
p1.stop_eating(food)
print(f"\nYour age is {p1.birth_year()}")