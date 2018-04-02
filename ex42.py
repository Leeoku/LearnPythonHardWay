## Animal is-a object (yes, sort of confusing, look at extra credit)

class Animal(object):
    pass

## Dog is an animal
class Dog(Animal):
    def __init__(self,name):
        ## ?? Dog has a name
        self.name = name
## Cat is an animal
class Cat(Animal):
    def __init__(self,name):
        ## cat has an init with param self, name
        self.name = name

## Person is an object
class Person(object):
    def __init__ (self, name):
        ## Person has an init with param self, name
        self.name = name
        ##Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):
    def __init__(self,name,salary):
        ## Employee has a name, salary
        super(Employee, self).__init__(name)
        ##Employee has an init with param name; Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has a pet named satan, From Mary, take the pet attribute and set to Satan
mary.pet = satan

## Frank is an employee with name Frank and salary 120000
frank = Employee("Frank", 120000)

##Fran is an Employee who is a person who has a pet attribute set to Rover
frank.pet = rover

##  Flipper is a fish
flipper = Fish()

## Crouse is a salmon
crouse = Salmon()

## Harry is an halibut
harry = Halibut()
