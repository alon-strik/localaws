## Logicly group a data and function for reuse
  ## attributes and methods assosiated with calss

# this is a class
class Employee:
    num_of_emps =0
    raise_amt = 1.04

    ## this is a constrctore or init method
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # decorator
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    ## use class method as alternative constractor
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


# this is class instance
# emp_1 = Employee('Alon','Strikovksy',5000)
# emp_2 = Employee('Chen','Elakbez',10000)
# print (emp_1.email)
# print (emp_2.email)
#action - call a method
##print(emp_1.fullname())
##print(emp_2.fullname())
# This is the same a above
##print(Employee.fullname(emp_1))
##print(Employee.fullname(emp_2))

## Here we use class method
# Employee.set_raise_amt(1.07)
#
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)


emp_str_1 = 'Alon-Strikovsky-200000'
new_emp_1 = Employee.from_string(emp_str_1)
print (new_emp_1.email)
print (new_emp_1.pay)
