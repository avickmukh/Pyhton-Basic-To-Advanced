'''
   Creating a Simple class in python
'''
   
class Person(object):
    __aadharCardNo = None
    def __init__(self, **kwargs):
        '''This method is similar like constructor'''
        self.__firstName = kwargs.get('firstName')
        self.__lastName = kwargs.get('lastName')
        self.__age = kwargs.get('age')
        if kwargs.get('aadharCardNo') != None :
            self.__aadharCardNo = kwargs.get('aadharCardNo')

    def print_info(self):
        '''This method will print information of person, it is a custom method'''
        print('information about the person')
        print('First Name = ', self.__firstName)
        print('last Name = ', self.__lastName)
        print('age Name = ', self.__age)
        print('Aadhar card Number = ', self.__aadharCardNo)
        print()

    def __str__(self):
        '''This method will invoke when we will print this class object'''
        return ' Person [FirstName = {}, LastName = {}, Age = {}, AadharCardNo = {}]'.format(
            self.__firstName,
            self.__lastName,
            self.__age,
            self.__aadharCardNo)

def person_test():
    p1 = Person(firstName = 'John', lastName = 'Doe', age = '30', aadharCardNo = 'dhaidhia')
    p1.print_info()
    p2 = Person(firstName = 'James', lastName = 'Bond', age = '26', aadharCardNo = 'uuajajja')
    print(p2)

if __name__ == '__main__' :
    person_test()