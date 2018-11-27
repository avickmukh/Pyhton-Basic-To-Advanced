'''
   Creating a Simple class in python
'''
   
class Person(object):
    __aadharCardNo = None
    def __init__(self, **kwargs):
        self.__firstName = kwargs.get('firstName')
        self.__lastName = kwargs.get('lastName')
        self.__age = kwargs.get('age')
        if kwargs.get('aadharCardNo') != None :
            self.__aadharCardNo = kwargs.get('aadharCardNo')


    def print_info(self):
        print('information about the person')
        print('First Name = ', self.__firstName)
        print('last Name = ', self.__lastName)
        print('age Name = ', self.__age)
        print('Aadhar card Number = ', self.__aadharCardNo)
        print()

    def __str__(self):
        return ' Person [FirstName = {}, LastName = {}, Age = {}, AadharCardNo = {}]'.format(
            self.__firstName,
            self.__lastName,
            self.__age,
            self.__aadharCardNo)

def person_test():
    p1 = Person(firstName = 'Avick', lastName = 'Mukherjee', age = '30', aadharCardNo = 'ihiqhiqhh')
    p1.print_info()
    p2 = Person(firstName = 'Arnab', lastName = 'Mukherjee', age = '26', aadharCardNo = 'uuajajja')
    print(p2)

if __name__ == '__main__' :
    person_test()