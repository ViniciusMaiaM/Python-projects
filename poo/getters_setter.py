class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discount(self,percentual):
        self.price = self.price - (self.price * (percentual/100))

    @property
    def price(self):
        return self.returned_price

    @property
    def name(self):
        return self.returned_name

#getter receives a value and setter configure it
#by convention you can't use the same name of variable to avoid problems

    @price.setter
    def price(self, value):
        if isinstance(value,str):
            value = float(value.replace('R$',''))
        self.returned_price = value

    @name.setter
    def name(self,new_name):
        self.returned_name = new_name.title()

#using the variable that was definided at the getter and using it        
#the function isinstace return true if the object is of the sprecified type

p1 = Product('shirt',"R$40")
p1.discount(10)
print(p1.name,p1.price)

#the title function turns the first letter upper