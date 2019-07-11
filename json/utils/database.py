import json

books_file = 'books.txt'

def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)

def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)
    #with open(books_file, 'a') as file:
     #   file.write(f'{name},{author},0')

    #books.append({'name':name, 'author': author, 'read': False})

def get_all_books():
    with open(books_file, 'r') as file:
       # lines = [line.strip().split(',') for line in file.readlines()]
        return json.load(file)
  #  return [
  #      {'name': line[0], 'author': line[1], 'read': line[2]}
   #     for line in lines
   # ]

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
        _save_all_books(books)

def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)
#        for book in books:
 #           file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

 #   for book in books:
  #      if book['name'] == name:
   #         books.remove(book)

