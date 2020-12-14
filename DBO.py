rom enum import Enum, auto

class Library:
    def __init__(self, address, name):
        self.address = address
        self.name = name

    def __str__(self):

        return '{}, {}'.format(self.address,self.name)

    def __eq__(self, other):
        equal = self.name == other.name
        equal = equal and self.address == other.address
        return equal

        
    
        
class Book:
    def __init__(self,code, title, publication_date, description, copies, author, publisher, state, genre, library):
        self.code = code
        self.title = title
        self.publication_date = publication_date
        self.description = description
        self.copies = copies
        self.author = author
        self.publisher =  publisher
        self.state =  state
        self.genre = genre
        self.library = library     



    def __str__(self):
        return '{},{},{},{},{},{},{},{},{},{}'.format(self.code, self.title, self.publication_date, self.description, self.copies, self.author, self.publisher, self.state, self.genre, self.library)

    def __eq__(self, other):
        return self.code == other.code

class Author:
    def __init__(self, name):
        self.name=name


    def __str__(self):
        return '{}'.format(self.name)

    def __eq__(self, other):
        return self.name == other.name


class Publisher:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return '{}'.format(self.name)

    def __eq__(self, other):
        return self.name == other.name
     

class State(Enum):
    AVAILABLE = 1
    REQUESTED = 2


class Genre(Enum):
    COMIC = 1
    SCIENCE = 2
