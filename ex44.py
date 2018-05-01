class Parent(object):

    def override(self):
        print("PARENT override()") 
    def implicit(self):
        print("PARENT implicit()")
    def altered (self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD AFTER PARENT altered()")

dad = Parent() #calls the parent class
son = Child() #calls the child class

dad.implicit() #returns Parent implicit, no override
son.implicit() #no child implicit, inherits parent implicit

dad.override() #returns Parent override
son.override() #returns Child override

dad.altered() #parent altered,
son.altered() #child before parent alter, parent altered, child after parent alter