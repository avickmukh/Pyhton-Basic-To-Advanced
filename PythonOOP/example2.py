'''
   working with properties in class
'''
   
class Person(object):
    __aadharCardNo = None
    def __init__(self, **kwargs):
        self.__firstName = kwargs.get('firstName')
        self.__lastName = kwargs.get('lastName')
        self.__age = kwargs.get('age')
        if kwargs.get('aadharCardNo') != None :
            self.__aadharCardNo = kwargs.get('aadharCardNo')

    def __str__(self):
        return ' Person [FirstName = {}, LastName = {}, Age = {}, AadharCardNo = {}]'.format(
            self.__firstName,
            self.__lastName,
            self.__age,
            self.__aadharCardNo)
    
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, value):
        self.__firstName = value

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, value):
        self.__lastName = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def aadharCardNo(self):
        return self.__aadharCardNo

    @aadharCardNo.setter
    def aadharCardNo(self, value):
        self.__aadharCardNo = value

    def __iadd__(self, value):
        if type(value) in (int, float):
            self.age += value
        elif type(value) == str:
            self.firstName += value
        return self

def main():
    p1 = Person(firstName = 'Avick', lastName = 'Mukherjee', age = 30, aadharCardNo = 'ihiqhiqhh')
    print(p1)
    print(p1.firstName)
    print(p1.lastName)
    print(p1.age)
    print(p1.aadharCardNo)

    p1.firstName = 'Anup'
    p1.age = 60
    p1.aadharCardNo = 'rqrqcafaf'

    print(p1)

    p1 += ' Kumar'
    p1 += 1

    print(p1)

if __name__ == '__main__' :
    main()