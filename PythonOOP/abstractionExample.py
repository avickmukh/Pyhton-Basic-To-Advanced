'''
   working with abstraction in python

   Here we will see basic calculator operation add, substraction, multiply, division
'''

from abc import ABC, abstractmethod
 
class AbstractOperation(ABC):
     
    def __init__(self, **kwargs):
        self.operatort1 = kwargs.get('operatort1')
        self.operatort2 = kwargs.get('operatort2')
        super(AbstractOperation, self).__init__()
    
    @abstractmethod
    def execute(self):
        pass
        
class AddOperation(AbstractOperation):
    def execute(self):
        return self.operatort1 + self.operatort2
 
 
class SubtractOperation(AbstractOperation):
    def execute(self):
        return self.operatort1 - self.operatort2
 
 
class MultiplyOperation(AbstractOperation):
    def execute(self):
        return self.operatort1 * self.operatort2
 
 
class DivideOperation(AbstractOperation):
    def execute(self):
        return int(self.operatort1 / self.operatort2)
        
def main():
    addOperation = AddOperation(operatort1 =1, operatort2 = 2)
    print("1 + 2 => ",addOperation.execute())

    subtractOperation = SubtractOperation(operatort1 = 5, operatort2 = 2)
    print("5 - 2 => ",subtractOperation.execute())

    multiplyOperation = MultiplyOperation(operatort1 = 6, operatort2 = 2)
    print("6 * 2 => ",multiplyOperation.execute())

    divideOperation = DivideOperation(operatort1 = 6, operatort2 =2)
    print("6 / 2 => ",divideOperation.execute())

if __name__ == '__main__' :
    main()