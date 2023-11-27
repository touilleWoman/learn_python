class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.name = f"{self.first} {self.last}"
        

tom = Person('Tom', 'Doe')
print(tom.name) # Tom Doe
tom.last = 'Smith'
print(tom.name) # Tom Doe
# Problem: name is not synchronized


class Person2:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def get_name(self):
        return f"{self.first} {self.last}"

tom = Person2('Tom', 'Doe')
print(tom.get_name()) # Tom Doe
tom.last = 'Smith'
print(tom.get_name()) # Tom Smith
# it works



# More elegent solution: use Property to do dynamic attribution

class Person3:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property 
    def name(self):
        return f"{self.first} {self.last}"
    
    
tom = Person3("Tom", "Doe")
print(tom.name)
tom.last = "Smith"
print(tom.name)