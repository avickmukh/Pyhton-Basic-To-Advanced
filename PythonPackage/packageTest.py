"""Include a own created package and use it

usage: 
    Python packageTest.py
"""
from animals.cat import Cat


def main():
    """Print Animal
    """
    catObject = Cat(vegetarian='veg', eats='milk', noOfLegs=4, color='white' )
    print(catObject)

#python packageTest.py 
if __name__ == '__main__' : main()