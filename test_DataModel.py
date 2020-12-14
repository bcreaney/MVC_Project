import pytest
from DBO import Library, Author, Publisher, Book, Genre, State
from DataModel import DataModel


# Testing add, delete and get Library

host  = 'localhost'
db    = 'teste'
user  = 'admin'
passw = 'admin'

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
	# setup
	model.setup_db()
	model.add_library(L1)
		
	# expect operation to fail
	assert model.add_book(B1) == False
	
	# cleanup
	model.clean_db()


def test_insert_duplicate_book():
	# setup
	model.setup_db()
	model.add_library(L1)
	model.add_author(A1)
	
	model.add_book(B1)
	# test
	assert model.add_book(B1) == False

	# cleanup
	model.clean_db()



def test_insert_duplicate_library():
	# setup
	model.setup_db()
	model.add_library(L1)
	# test
	assert model.add_library(L1) == False
	# cleanup
	model.clean_db()

	

def test_insert_duplicate_author():
	# setup
	model.setup_db()
	model.add_author(A1)
	# test
	assert model.add_author(A1) == False
	# cleanup
	model.clean_db()
	

def test_del_nonexistent_book():
	# setup
	model.setup_db()
	# test
	assert model.del_author(A1) == True
	# cleanup
	model.clean_db()


def test_del_nonexistent_lib():
	# setup
	model.setup_db()
	# test
	assert model.del_library(L1) == True
	# cleanup
	model.clean_db()



def test_del_nonexistent_author():
	# setup
	model.setup_db()
	# test
	assert model.del_author(L1) == True
	# cleanup
	model.clean_db()

def test_set_get_authors():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_author(A2)
	# test:
	authors = model.get_authors()

	assert A1 in authors and A2 in authors

	# cleanup
	model.clean_db()



def test_set_get_libs():
	# setup:
	model.setup_db()
	model.add_library(L1)
	model.add_library(L2)
	# test:
	libs = model.get_libraries()
	assert L1 in libs and L2 in libs
	# cleanup
	model.clean_db()


def test_set_get_books():
	# setup:
	model.setup_db()
	# test:
	model.add_book(B1)
	assert model.add_book(B1) == False
	# cleanup
	model.clean_db()


def test_get_books_by_author():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_author(A1)
	assert B1 in books
	# cleanup
	model.clean_db()

def test_get_books_by_author_nonexistent():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books=model.get_books_by_author(A2)
	assert books == []
	# cleanup
	model.clean_db()



def test_get_books_by_genre():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_genre(1)
	assert B1 in books

	# cleanup
	model.clean_db()

def test_get_books_by_genre_nonexistent():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_genre(6)
	assert books == []

	# cleanup
	model.clean_db()

def test_get_books_by_year():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_year(2020)
	assert B1 in books

	# cleanup
	model.clean_db()

def test_get_books_by_year_nonexistent():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_year(2021)
	assert books == []
	# cleanup
	model.clean_db()
	
def test_get_books_by_library():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	model.add_book(B2)
	# test:
	books = model.get_books_by_library(L1)
	assert B1 in books and B2 in books
	# cleanup
	model.clean_db()

def test_get_books_by_library_nonexistent():
	# setup: 
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test: 
	books = model.get_books_by_library(L2)
	assert books == []
	# cleanup
	model.clean_db()


def test_get_books_by_state():
	# setup: 
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_state(1)
	assert B1 in books
	# cleanup
	model.clean_db()

def test_get_books_by_state_nonexistent():
	# setup: 
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_state(6)
	assert B1 not in books
	# cleanup
	model.clean_db()

def test_get_books_by_publisher():
	# setup: 
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	model.add_book(B2)
	# test:
	books = model.get_books_by_publisher(P1)
	assert B1 in books
	# cleanup
	model.clean_db()

def test_get_books_by_publisher_nonexistent():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	books = model.get_books_by_publisher(P2)
	assert books == []
	# cleanup
	model.clean_db()

def test_get_book():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	book = model.get_book(1408870584)
	assert book == B1
	# cleanup
	model.clean_db()


def test_get_library():
	# setup:
	model.setup_db()
	model.add_library(L1)
	# test:
	lib = model.get_library('Bananas library')
	assert lib == L1
	# cleanup
	model.clean_db()

def test_get_nonexistent_library():
	# setup:
	model.setup_db()
	# test:
	lib = model.get_library('lala library')
	assert lib == []
	# cleanup
	model.clean_db()

def test_get_genres():
	# setup:
	model.setup_db()
	# test:
	assert model.get_genres() == [(1,),(2,)]
	model.clean_db()



def test_get_states():
	# setup:
	model.setup_db()
	# test:
	assert model.get_states() == [(1,),(2,)]
	model.clean_db()


def test_get_publisher():
	# setup:
	model.setup_db()
	model.add_publisher(P1)
	# test:
	pub = model.get_publisher('Publisher Sol')
	assert pub == P1
	# cleanup
	model.clean_db()


def test_get_nonexistent_publisher():
	# setup:
	model.setup_db()
	# test:
	pub = model.get_publisher('abc')
	assert pub == []
	# cleanup
	model.clean_db()

def test_get_author():
	# setup:
	model.setup_db()
	model.add_author(A1)
	# test:
	a = model.get_author('Bia dos morangos')
	assert  a == A1
	# cleanup
	model.clean_db()

def test_get_nonexistent_author():
	# setup:
	model.setup_db()
	# test:
	a = model.get_author('Bia sorte')
	assert a == []
	# cleanup
	model.clean_db()

################################################

def test_get_nonexistent_book():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	assert model.get_book(1408870555) == None
	# cleanup
	model.clean_db()


def test_del_book():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	assert model.del_book(B1) == True
	# cleanup
	model.clean_db()

def test_del_nonexistent_book():
	# setup:
	model.setup_db()
	# test:
	assert model.del_book(B2) == True
	# cleanup
	model.clean_db()

def test_del_author_with_NO_books_associated():
# setup:
	model.setup_db()
	# test:
	assert model.del_author(A2) == True
	# cleanup
	model.clean_db()


def test_del_author_with_books_associated():
# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	assert model.del_author(A1) == False
	# cleanup
	model.clean_db()

def test_update_to_new_state():
	# setup:
	model.setup_db()
	# test:
	assert model.update_state(2,B1) == True
	# cleanup
	model.clean_db()

def test_update_to_SAME_state():
	# setup:
	model.setup_db()
	# test:
	assert model.update_state(1,B1) == True
	# cleanup
	model.clean_db()


def test_update_book_library():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_library(L2)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	assert model.update_library(L2,B1) == True
	# cleanup
	model.clean_db()


def test_update_book_to_nonexisting_library():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
	assert model.update_library(L2,B1) == False
	# cleanup
	model.clean_db()

def test_add_1_copy_to_book():
	# setup:
	model.setup_db()
	model.add_author(A1)
	model.add_library(L1)
	model.add_publisher(P1)
	model.add_book(B1)
	# test:
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
