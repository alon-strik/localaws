## Logicly group a data and function for reuse
  ## attributes and methods assosiated with calss

# this is a class
class Employee:
    ## this is a constrctore or init method
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


# this is class instance
emp_1 = Employee('Alon','Strikovksy',5000)
emp_2 = Employee('Chen','Elakbez',10000)
# print (emp_1.email)
# print (emp_2.email)

#action - call a method
print(emp_1.fullname())
print(emp_2.fullname())
# This is the same a above
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))