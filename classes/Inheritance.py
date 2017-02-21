#https://www.youtube.com/watch?v=RSl87lqOXDE
#
# for i in range(1,48, 6):
#     print i

# Base class
class Person(object):
    def __init__(self, name):
        self.name = name

    def identity(self):
        print "My name is {}".format(self.name)


# This class inharets from Person class
class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def identity(self):
        super(SuperHero, self).identity()
        print "...And I am {}".format(self.hero_name)


###

print (help(SuperHero))
# corry = Person('Corry')
# corry.identity()

# wade = SuperHero('Corry Smith','Batman')
# wade.identity()