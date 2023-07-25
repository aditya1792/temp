'''
    Operator Overloading in python
'''

class Employee:
    def __init__(self, p):
        self.price = p
 
    def __lt__(self, other):
        return self.price < other.price
        
    def __gt__(self, other):
        if(self.price > other.price):
            return True
        else:
            return False

    def __le__(self, other):
        if(self.price <= other.price):
            return True
        else:
            return False
        
        
emp1 = Employee(int(input("Salary of employee 1: ")))
emp2 = Employee(int(input("Salary of employee 2: ")))

if(emp1 < emp2):
    print('\n emp1 is lesser ')
else:
    print('\n emp2 is lesser ')

    
if(emp1 > emp2):
    print('\n emp1 is greater ')
else:
    print('\n emp2 is greater ')


if(emp1 <= emp2):
    print('\n emp1 is lesser or equal ')
else:
    print('\n emp2 is lesser or equal')
