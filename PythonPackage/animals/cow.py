from animals.animal import Animal

class Cow(Animal):
    
    def __init__(self, **kwargs):
        self.vegetarian = kwargs.get('vegetarian')
        self.eats = kwargs.get('eats')
        self.noOfLegs = kwargs.get('noOfLegs')
        self.color = kwargs.get('color')

    def __str__(self):
        return self.color