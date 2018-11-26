class Animal:
    
    def __init__(self, **kwargs):
        print('init method called from Animal')
        self.vegetarian = kwargs.get('vegetarian')
        self.eats = kwargs.get('eats')
        self.noOfLegs = kwargs.get('noOfLegs')

    def __str__(self):
        return self.vegetarian + " " + self.eats + " " + self.noOfLegs