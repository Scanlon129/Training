# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods

# Class attributes and methods used here are shared at the class level which applies to all
# subclasses and instances created from this class.

# Static methods are

class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or
    # class-specific
    @staticmethod #this is referred to as a decorator
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # class methods receive a class as their argument and can only
    # operate on class-level data
    @classmethod #this is referred to as a decorator
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

# TODO: access the class attribute
print("Book Types: ", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
# THIS NEEDS FURTHER UNDERSTANDING