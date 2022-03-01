# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
        #Each attribute is called an instance attribute since it is unique
        #this instance

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
                return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        self._discount = amount
    #Notice! that the discount attribute has a "_" in front of it. That is to
    #give other developers a hint that this attribute is only to be referenced
    #within the class, is internal to the class, and should not be accessed
    #outside the classes logic.

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Things They Carried", "Tim Obrien", 233, 15.99)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
#print(b2.__secret) - This will throw an error - python does this to prevent subclasses from overriding this attribute.
print(b2._Book__secret)
#Using a double underscore will create a secret attribute within a class (see the Book class above)