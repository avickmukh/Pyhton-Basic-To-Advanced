from animals.animal import Animal

class Cat(Animal):
    
    def __init__(self, **kwargs):
        print('init method called')
        self.vegetarian = kwargs.get('vegetarian')
        self.eats = kwargs.get('eats')
        self.noOfLegs = kwargs.get('noOfLegs')
        self.color = kwargs.get('color')

    def __str__(self):
        return self.color