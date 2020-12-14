from flask import Flask, redirect, url_for, render_template, request, abort, Response
from DBO import Library, Author, Publisher, Book, Genre, State
from DataModel import DataModel
import json as json


app = Flask(__name__)

host  = 'localhost'
db    = 'teste'
user  = 'admin'
passw = 'admin'

model = DataModel(host, user, db, passw)


@app.route("/books",methods=["GET", "POST"])
def all_books():
    if request.method == "GET":
        books = model.get_books()
        return json.dumps([b.__dict__ for b in books])
    
    elif request.method == "POST":
        print("YEYYY vou criar um livro!!!")
        content = request.get_json(silent=True)
        if not content:
            print("vazio???")
            abort(400)

        print(content)
        code = content['code']
        title = content['title']
        publication_date = content['publication_date']
        description = content['description']
        copies = content['copies']
        author = content['author']
        publisher = content['publisher']
        state = content['state']
        genre = content['genre']
        library = content['library']

        b = Book(code, title, publication_date,description,copies,author,publisher,state,genre,library)
        if model.add_book(b) == False:
            abort(418)

        return Response('', 200)

@app.route("/books/<code>",methods=["GET","DELETE","PUT"])
def book(code):

    book = model.get_book(code)
    if book is None:
        abort(404)

    if request.method == "GET":
        return json.dumps(book.__dict__)
    
    elif request.method == "DELETE":
        ok = model.del_book(code)
        if not ok:
            abort(500)
        return Response('', status=200, mimetype='application/json')

    elif request.method == "PUT":
        content = request.get_json(silent=True)
        if not content:
            print("vazio???")
            abort(400)

        req_code = content['code']
        if int(code) != int(req_code):
            abort(422)

        title = content['title']
        publication_date = content['publication_date']
        description = content['description']
        copies = content['copies']
        author = content['author']
        publisher = content['publisher']
        state = content['state']
        genre = content['genre']
        library = content['library']

        b = Book(code, title, publication_date,description,copies,author,publisher,state,genre,library)
        if model.update_state(b) == False:
            abort(500)
        return Response('', status=200, mimetype='application/json')


    

@app.route("/libraries",methods=["GET","POST"])
def all_libraries():
    if request.method == "GET":
        libraries = model.get_libraries()
        return json.dumps([l.__dict__ for l in libraries])

    elif request.method == "POST":
        content = request.get_json(silent=True)
        if not content:
            abort(400)

        address = content['address']
        name = content['name']
    
        l = Library(address, name)
        if model.add_library(l) == False:
            abort(418)

        return Response('', 200)


@app.route("/libraries/<name>",methods=["GET","DELETE"])
def return_library(name):
    library = model.get_library(name)
    if library is None:
        abort(404)

    if request.method == "GET":
        return json.dumps(library.__dict__)

    elif request.method == "DELETE":
        ok = model.del_library(name)
        if not ok:
            abort(500) 
        return Response('', status=200, mimetype='application/json')
        


@app.route("/genres",methods=["GET"])
def get_genres():
    genres = model.get_genres()
    return json.dumps([g for g in genres])

@app.route("/states",methods=["GET"])
def get_states():
    states = model.get_states()
    return json.dumps([s for s in states])

@app.route("/publishers",methods=["GET","POST"])
def all_publishers():
    if request.method == "GET":
        publishers = model.get_publishers()
        return json.dumps([p.__dict__ for p in publishers])

    elif request.method == "POST":
        content = request.get_json(silent=True)
        if not content:
            abort(400)

        name = content['name']
    
        p = Publisher(name)
        if model.add_publisher(p) == False:
            abort(418)

        return Response('', 200)

@app.route("/publishers/<name>",methods=["GET","DELETE"])
def return_publisher(name):
    publisher = model.get_publisher(name)
    if publisher is None:
        abort(404)

    if request.method == "GET":
        return json.dumps(publisher.__dict__)
    elif request.method == "DELETE":
        ok = model.del_publisher(name)
        if not ok:
            abort(500) 
        return Response('', status=200, mimetype='application/json')


@app.route("/authors",methods=["GET", "POST"])
def all_authors():
    if request.method == "GET":
        authors = model.get_authors()
        return json.dumps([a.__dict__ for a in authors])

    elif request.method == "POST":
        content = request.get_json(silent=True)
        if not content:
            abort(400)

        name = content['name']
    
        a = Author(name)
        if model.add_author(a) == False:
            abort(418)

        return Response('', 200)

       

@app.route("/authors/<name>",methods=["GET", "DELETE"])
def return_author(name):

    author = model.get_author(name)
    if author is None:
        abort(404)

    if request.method == "GET":
        return json.dumps(author.__dict__)

    elif request.method == "DELETE":
        ok = model.del_author(name)
        if not ok:
            abort(500) 
        return Response('', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run()
