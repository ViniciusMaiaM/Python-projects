class Coffe:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price) 
    
    def check_budget(self,budget):
        if not isinstance(budget,(int,float)):
            print("Please enter float or int")
            exit()
        if budget < 0:
            print("Sorry you dont have money")
            exit()

    def get_change(self,budget):
        return budget - self.price
    
    def sell(self,budget):
        self.check_budget(budget)
        if budget >= self.price:
            print(f"\nYou can buy the {self.name} Coffe\n")
            if budget == self.price:
                print("You've buyed it!\n")
            else:
                print(f"Here is your change {self.get_change(budget)}$\n")
            exit("Thanks!!\n")

small = Coffe('Small',2.50)
regular = Coffe('Regular',5.50)
big = Coffe('Big',6.50)

print('''
|--------------------------------------------|
|    Hey, welcome let's get you a Coffe!!    |
|--------------------------------------------|
|  Small: 2.50  Regular: 5.50   Large: 6.50  |
|--------------------------------------------|''')

try:
    user_budget = float(input("What's your budget? "))
except ValueError:
    exit("Please enter a number!")

for Coffe in [small,regular,big]:
    Coffe.sell(user_budget)
