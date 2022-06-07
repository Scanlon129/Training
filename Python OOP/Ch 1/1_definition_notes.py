# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions

# TODO: create a basic class
class Book:
    def __init__(self, title):
        self.title = title
    #The __init__ function is a special function to use while working with classes.
    #Used to initialize attributes.
    #In this case we pass in title.

#can also define class as 'class Book():' if it will inherit from another class.

# TODO: create instances of the class
b1 = Book('Brave New World')
b2 = Book('The Things They Carried')
#Note - we only pass one argument in since the 'self' parameter is 
#Whenever we call a method on a python object, the object itself automatically 
#gets passed in as the first object. 

# TODO: print the class and property
print(b1)
print(b1.title)