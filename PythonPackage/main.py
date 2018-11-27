"""Include a own created package and use it

usage: 
    Python main.py
"""
from animals import cat, cow


def main():
    """Print Animal
    """
    catObject = cat.Cat(vegetarian='non', eats='milk', noOfLegs=4, color='white' )
    print(catObject)
    cowObject = cow.Cow(vegetarian='', eats='grass', noOfLegs=4, color='brown' )
    print(cowObject)

#python packageTest.py 
if __name__ == '__main__' : main()