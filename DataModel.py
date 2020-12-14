import mysql.connector
from mysql.connector import Error
from enum import Enum, auto
from DBO import Library, Author, Publisher, Book, Genre, State

class DataModel:
    def __init__(self, host, user, db, passw):

        try:
            self.connection = mysql.connector.connect(host=host,
                                                      user=user,
                                                      database=db,
                                                      password=passw)
            self.cursor = self.connection.cursor()
        except:
            self.connection = mysql.connector.connect(host=host,
                                                      user=user,
                                                      password=passw)
            self.cursor = self.connection.cursor()
            self.cursor.execute("CREATE DATABASE " + db)


        self.connection = mysql.connector.connect(host=host,
                                                  user=user,
                                                  database=db,
                                                  password=passw)
        self.cursor = self.connection.cursor()


    def setup_db(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS Book")
            self.cursor.execute("DROP TABLE IF EXISTS Library")
            self.cursor.execute("DROP TABLE IF EXISTS State")
            self.cursor.execute("DROP TABLE IF EXISTS Genre")
            self.cursor.execute("DROP TABLE IF EXISTS Publisher")
            self.cursor.execute("DROP TABLE IF EXISTS Author")


            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Author (name VARCHAR(255) NOT NULL PRIMARY KEY)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Publisher (name VARCHAR(100) NOT NULL PRIMARY KEY)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Genre (value INTEGER NOT NULL PRIMARY KEY)""")
            query1 = "INSERT INTO Genre (value) VALUES ('" + str(Genre.COMIC.value) + "'), ('" + str(Genre.SCIENCE.value) + "')"
            self.cursor.execute(query1)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS State (value INTEGER  NOT NULL PRIMARY KEY)""")
            query2 = "INSERT INTO State (value) VALUES ('" + str(State.AVAILABLE.value) + "'),('" + str(State.REQUESTED.value) + "')"
            self.cursor.execute(query2)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Library (address VARCHAR(255) NOT NULL,name VARCHAR(100) NOT NULL PRIMARY KEY)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Book (
            code INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            publication_date INTEGER NOT NULL,
            description TEXT NOT NULL,
            copies INTEGER NOT NULL,
            
            library VARCHAR(100) NOT NULL,
            FOREIGN KEY(library) REFERENCES Library(name),
            
            genre INTEGER NOT NULL,
            FOREIGN KEY(genre) REFERENCES Genre(value),
            
            state INTEGER NOT NULL,
            FOREIGN KEY(state) REFERENCES State(value),

            author VARCHAR(255) NOT NULL,
            FOREIGN KEY(author) REFERENCES Author(name),
            
            publisher VARCHAR(100) NOT NULL,
            FOREIGN KEY(publisher) REFERENCES Publisher(name))""")

            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False 

    def clean_db(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS Book")
            self.cursor.execute("DROP TABLE IF EXISTS Library")
            self.cursor.execute("DROP TABLE IF EXISTS State")
            self.cursor.execute("DROP TABLE IF EXISTS Genre")
            self.cursor.execute("DROP TABLE IF EXISTS Publisher")
            self.cursor.execute("DROP TABLE IF EXISTS Author")

            return True
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False 
 


    def add_library(self,lib):
        try:
            query = "INSERT INTO Library (address, name) VALUES (%s, %s)"
            val = (lib.address, lib.name)
            self.cursor.execute(query, val)
            self.connection.commit()
            print(str(lib.name) + ' added successfully')
            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False


    def del_library(self, library):
        try:
            query = "DELETE FROM Library WHERE name = %s"
            self.cursor.execute(query, (library.name,))
            self.connection.commit()
            print(str(library.name) + ' deleted successfully')
            return True
        
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False


    def genre_to_str(self, genre):
        if genre == Genre.COMIC:
            return 'COMIC'
        elif genre == Genre.SCIENCE:
            return "SCIENCE"
    
    def state_to_str(self, state):
        if state == State.AVAILABLE:
            return 'AVAILABLE'
        elif state == State.REQUESTED:
            return "REQUESTED"

    def get_genres(self):
        query = "SELECT * FROM Genre"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(self.genre_to_str(Genre(i[0])))
        return l

    def get_states(self):
        query = "SELECT * FROM State"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(self.state_to_str(State(i[0])))
        return l


    def get_libraries(self):
        query = "SELECT address, name FROM Library"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Library(i[0],i[1]))
        return l


    def get_library(self,name):
        try:
            query = "SELECT address, name FROM Library WHERE name = %s"
            self.cursor.execute(query, (name,))
            myresult = self.cursor.fetchall()
            l=None
            if len(myresult) != 0:
                l = Library(myresult[0][0],myresult[0][1])
            return l
    
        
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False



    def add_author(self, author):
        try:
            query = "INSERT INTO Author (name) VALUES (%s)"
            val = (author.name,)
            self.cursor.execute(query, val)
            self.connection.commit()
            print(str(author.name) + ' added successfully')
            
            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

            return False

       
    def get_authors(self):
        query = "SELECT * FROM Author"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Author(i[0]))
        return l

        


    def get_author(self,name):
        try:
            query = "SELECT * FROM Author WHERE name = (%s)"
            val = (name,)
            self.cursor.execute(query, val)
            myresult = self.cursor.fetchall()
            print(myresult)
            l=None
            if len(myresult) != 0:
                l = Author(myresult[0][0])
            return l

        except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                return False
     
    def add_publisher(self,publisher):
        
        try:
            query = "INSERT INTO Publisher (name) VALUES (%s)"
            val = (publisher.name,)
            self.cursor.execute(query, val)
            self.connection.commit()

            print(str(publisher.name) + ' added successfully')
            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False



    def get_publishers(self):
        query = "SELECT * FROM Publisher"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Publisher(i[0]))
        return l


    def get_publisher(self, name):
        query = "SELECT * FROM Publisher WHERE name = %s"
        self.cursor.execute(query, (name,)) 
        myresult = self.cursor.fetchall()
        l = None
        if len(myresult) != 0:
            l = Publisher(myresult[0][0])
        return l


    def add_book(self,book):
        try:
            query = "INSERT INTO Book (code,title,publication_date,description, copies, author, publisher, state, genre, library) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (book.code, book.title, book.publication_date, book.description, book.copies, book.author, book.publisher, book.state,  book.genre, book.library)
            self.cursor.execute(query, val)
            self.connection.commit()
            print(str(book.title) + ' added successfully')
            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

    def get_books(self):
        query = "SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        l=[]
        if len(myresult) !=0:
            for i in myresult:
                l.append(Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
        return l



    def get_books_by_author(self, author):
        query = ("SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book WHERE author = (%s) ")
        val = (author.name,)
        self.cursor.execute(query, val)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
        return l


    def get_books_by_genre(self, genre):
       
        query = ("SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book WHERE genre = (%s) ")
        val = (genre,)
        self.cursor.execute(query, val)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
        return l   



    def get_books_by_year(self, year):
        
        query = ("SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book WHERE publication_date = (%s) ")
        val = (year,)
        self.cursor.execute(query, val)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
        return l   


    

    def get_books_by_library(self,library):
       
        query = ("SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book WHERE library = (%s) ")
        val = (library.name,)
        self.cursor.execute(query, val)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
        return l 
       

    def get_books_by_state(self,state):
        
        query = ("SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book WHERE state = (%s) ")
        val = (state,)
        self.cursor.execute(query, val)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
        return l 


    def get_books_by_publisher(self,publisher):
        query = ("SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book WHERE publisher = (%s) ")
        val = (publisher.name,)
        self.cursor.execute(query, val)
        myresult = self.cursor.fetchall()
        l=[]
        for i in myresult:
            l.append(Book(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
        return l 


    def get_book(self, code):

        query = "SELECT code,title,publication_date,description, copies, author, publisher, state, genre, library FROM Book WHERE code = (%s)"
        val = (code,)
        self.cursor.execute(query, val)
        myresult = self.cursor.fetchall()
        print(myresult)
        if len(myresult) != 0:
            b = Book(myresult[0][0],myresult[0][1],myresult[0][2],myresult[0][3],myresult[0][4],myresult[0][5],myresult[0][6],myresult[0][7],myresult[0][8],myresult[0][9])
            return b
    

    def del_book(self,code):
        try:
            query = "DELETE FROM Book WHERE code = (%s)"
            val = (code,)
            self.cursor.execute(query, val)
            self.connection.commit()
            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

    def del_author(self,name):
        try:
            query = "DELETE FROM Author WHERE name = (%s)"
            val = (name,)
            self.cursor.execute(query, val)
            self.connection.commit()
            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

    def del_publisher(self,publisher):
        try:
            query = "DELETE FROM Publisher WHERE name = (%s)"
            val = (name,)
            self.cursor.execute(query, val)
            self.connection.commit()
            return True

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

    
    def update_state(self,book):
        try:
            query = "UPDATE Book SET title = (%s),publication_date= (%s),description= (%s), copies= (%s), author= (%s), publisher= (%s), state= (%s), genre= (%s), library = (%s) WHERE code = (%s)"
            val = (book.title,book.publication_date,book.description, book.copies, book.author, book.publisher, book.state, book.genre, book.library, book.code,)
            self.cursor.execute(query, val)
            self.connection.commit()
            print('state updated')
            return True
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False


    def add_book_copy(self, book):
        try:
            query = "UPDATE Book SET copies = (%s) WHERE code = (%s)"
            val = (book.copies+1, book.code,)
            self.cursor.execute(query, val)
            self.connection.commit()
            print('added 1 copy to the book')
            return True
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False
