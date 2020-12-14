import pytest
from DBO import Library, Author, Publisher, Book, Genre, State
from DataModel import DataModel


host  = #add here
db    = #add here
user  = #add here
passw = #add here

model = DataModel(host, user, db, passw)

def test_book_without_lib():
	# setup test
	model.setup_db()
	model.add_author(A1)
	model.add_publisher(P1)

	# expect operation to fail
	assert model.add_book(B1) == False

	# cleanup
	model.clean_db()



def test_book_without_author():
	model.setup_db()
	model.add_library(L1)
	assert model.add_book(B1) == False
	model.clean_db()


def test_insert_duplicate_book():
	model.setup_db()
	model.add_library(L1)
	model.add_author(A1)
	model.add_book(B1)
	assert model.add_book(B1) == False
	model.clean_db()



def test_insert_duplicate_library():
	model.setup_db()
	model.add_library(L1)
	assert model.add_library(L1) == False
  model.clean_db()

	

def test_insert_duplicate_author():
	model.setup_db()
	model.add_author(A1)
	assert model.add_author(A1) == False
	model.clean_db()
	

def test_del_nonexistent_book():
	model.setup_db()
	assert model.del_author(A1) == True
	model.clean_db()


def test_del_nonexistent_lib():
	model.setup_db()
	assert model.del_library(L1) == True
	model.clean_db()



def test_del_nonexistent_author():
	model.setup_db()
	assert model.del_author(L1) == True
	model.clean_db()

def test_set_get_authors():

	model.setup_db()
	model.add_author(A1)
	model.add_author(A2)
	authors = model.get_authors()
  assert A1 in authors and A2 in authors
	model.clean_db()



def test_set_get_libs():

	model.setup_db()
	model.add_library(L1)
	model.add_library(L2)
	libs = model.get_libraries()
	assert L1 in libs and L2 in libs
	model.clean_db()


def test_set_get_books():
	
	model.setup_db()
	model.add_book(B1)
	assert model.add_book(B1) == False
	model.clean_db()


def test_get_books_by_author():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_author(A1)
	assert B1 in books
	model.clean_db()

def test_get_books_by_author_nonexistent():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books=model.get_books_by_author(A2)
	assert books == []
	model.clean_db()



def test_get_books_by_genre():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_genre(1)
	assert B1 in books
	model.clean_db()

def test_get_books_by_genre_nonexistent():

	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_genre(6)
	assert books == []
	model.clean_db()

def test_get_books_by_year():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_year(2020)
	assert B1 in books
	model.clean_db()

def test_get_books_by_year_nonexistent():

	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_year(2021)
	assert books == []
	model.clean_db()
	
def test_get_books_by_library():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	model.add_book(B2)
	books = model.get_books_by_library(L1)
	assert B1 in books and B2 in books
	model.clean_db()

def test_get_books_by_library_nonexistent():
 
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_library(L2)
	assert books == []
	model.clean_db()


def test_get_books_by_state():
 
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_state(1)
	assert B1 in books
	model.clean_db()

def test_get_books_by_state_nonexistent():
 
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)

	books = model.get_books_by_state(6)
	assert B1 not in books

	model.clean_db()

def test_get_books_by_publisher():

	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	model.add_book(B2)
	books = model.get_books_by_publisher(P1)
	assert B1 in books
	model.clean_db()

def test_get_books_by_publisher_nonexistent():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	books = model.get_books_by_publisher(P2)
	assert books == []
	model.clean_db()

def test_get_book():

	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	book = model.get_book(1408870584)
	assert book == B1
	model.clean_db()


def test_get_library():
	
	model.setup_db()
	model.add_library(L1)
	lib = model.get_library('Bananas library')
	assert lib == L1
	model.clean_db()

def test_get_nonexistent_library():

	model.setup_db()
	lib = model.get_library('lala library')
	assert lib == []
	model.clean_db()

def test_get_genres():

	model.setup_db()
	assert model.get_genres() == [(1,),(2,)]
	model.clean_db()


def test_get_states():

	model.setup_db()
	assert model.get_states() == [(1,),(2,)]
	model.clean_db()


def test_get_publisher():

	model.setup_db()
	model.add_publisher(P1)
	pub = model.get_publisher('Publisher Sol')
	assert pub == P1
	model.clean_db()


def test_get_nonexistent_publisher():
	
	model.setup_db()
	pub = model.get_publisher('abc')
	assert pub == []
	model.clean_db()

def test_get_author():

	model.setup_db()
	model.add_author(A1)
	a = model.get_author('Bia dos morangos')
	assert  a == A1
	model.clean_db()

def test_get_nonexistent_author():
	
	model.setup_db()
	a = model.get_author('Bia sorte')
	assert a == []
	model.clean_db()


def test_get_nonexistent_book():

	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	assert model.get_book(1408870555) == None
	model.clean_db()


def test_del_book():

	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	assert model.del_book(B1) == True
	model.clean_db()

def test_del_nonexistent_book():

	model.setup_db()
	assert model.del_book(B2) == True
	model.clean_db()

def test_del_author_with_NO_books_associated():

	model.setup_db()
	assert model.del_author(A2) == True
	model.clean_db()


def test_del_author_with_books_associated():

	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	assert model.del_author(A1) == False
	model.clean_db()

def test_update_to_new_state():
	
	model.setup_db()
	assert model.update_state(2,B1) == True
	model.clean_db()

def test_update_to_SAME_state():

	model.setup_db()
	assert model.update_state(1,B1) == True
	model.clean_db()


def test_update_book_library():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_library(L2)
	model.add_publisher(P1)
	model.add_book(B1)
	
	assert model.update_library(L2,B1) == True

	model.clean_db()


def test_update_book_to_nonexisting_library():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)

	assert model.update_library(L2,B1) == False

	model.clean_db()

def test_add_1_copy_to_book():
	
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)

	assert model.add_book_copy(B1) == True
	model.clean_db()

def test_setup_db():
	assert model.setup_db() == True
	model.clean_db()

def test_add_library():
	model.setup_db()
	assert model.add_library(L1) == True
	model.clean_db()

def test_del_library():
	model.setup_db()
	assert model.del_library(L1) == True
	model.clean_db()

def test_add_author():
	model.setup_db()
	assert model.add_author(A1) == True
	model.clean_db()

def test_add_publisher():
	model.setup_db()
	assert model.add_publisher(P1) == True
	model.clean_db()

def test_add_book():
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	assert model.add_book(B1) == True
	model.clean_db()
