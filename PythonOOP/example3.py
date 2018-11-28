'''
   working with inheritance in python
'''
   
class Person(object):
    def __init__(self, **kwargs):
        self._name = kwargs.get('name')
        self._email = kwargs.get('email')
        self._phone = kwargs.get('phone')
        print('Person Init Method Called')

    def __str__(self):
        return ' Person [name = {}, email = {}, phone = {}]'.format(
            self._name,
            self._email,
            self._phone)
    
class Resource(object):
    _resourceId = None
    _location = 'Bangalore'

    def __init__(self, **kwargs):
        self._resourceId = kwargs.get('resourceId')
        self._location = kwargs.get('location')
        print('Resource Init Method Called')

    def __str__(self):
        return ' Resource [resourceId = {}, location = {}]'.format(
            self._resourceId,
            self._location)

class Employee(Person, Resource):
    def __init__(self, **kwargs):
        # super.__init__(**kwargs)
        Person.__init__(self, **kwargs)
        Resource.__init__(self, **kwargs)
        print('Employee Init Method Called')

    def __str__(self):
        return ' Employee [resourceId = {}, location = {}, name = {}, email = {}, phone = {}]'.format(
            self._resourceId,
            self._location,
            self._name,
            self._email,
            self._phone) 


def main():
    employee1 = Employee(name = 'Avick Mukherjee', email = 'avickmukh@gmail.com', phone = '998899887', location='Bangalore', resourceId='1')
    #print(dir(employee1))
    print(employee1)

if __name__ == '__main__' :
    main()