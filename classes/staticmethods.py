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

    @staticmethod
    def is_weekday(day):
        # Fridey =5 Saturday = 6
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


# this is class instance
emp_1 = Employee('Alon','Strikovksy',5000)
emp_2 = Employee('Chen','Elakbez',10000)

import datetime
my_date = datetime.date(2017, 2, 18)
print(Employee.is_weekday(my_date))