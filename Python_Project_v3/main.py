from recommended_books import recommend_books
from Books import Book
from add_book_dynamically import add_books_from_csv

class User:

    def __init__(self, name , user_id , borrowed_books):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = list(borrowed_books)

    def return_book_user(self,isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

    def borrow_book_user(self,isbn):
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
            return True
        return False

    def show_user(self):
        print(f"Name: {self.name} , ID: {self.user_id} , Borrowed Books: {self.borrowed_books}")


class Library:

    def __init__(self):
        self.book = {}
        self.user = {}

    def add_book(self,book):
        self.book[book.isbn] = book
        print(f"{book} added to library")

    def add_user(self,user):
        self.user[user.user_id] = user
        print(f"Name: {user.name}, User_ID: {user.user_id} added to library")

    def user_borrow(self,user_id,isbn):
     if user_id in self.user:
        if isbn in self.book:
            b = self.book[isbn]
            u = self.user[user_id]
            if b.borrow_book():
             if u.borrow_book_user(isbn):
              print(f"User_ID: {user_id} borrowed book ISBN: {isbn}")
              return True
             else:
              b.return_book()
              print(f"User_ID {user_id} already has ISBN: {isbn}")
            else:
                print(f"ISBN: {isbn} book is not available")
        else:
            print(f"ISBN: {isbn} book is not available")
     else:
         print(f"User_ID: {user_id} does not exist")
     return False

    def user_return_borrow(self,user_id,isbn):
       if user_id in self.user:
        if isbn in self.book:
         u = self.user[user_id]
         b = self.book[isbn]
         if u.return_book_user(isbn):
          if b.return_book():
           print(f"User_ID: {user_id} returned book ISBN: {isbn}")
          else:
           print("Book is not returned")
         else:
           print("Already returned")
        else:
           print(f"User_ID: {user_id} does not exist")
       else:
         print(f"ISBN: {isbn} book is not available")
       return False

    def display_all_books(self):
        for i in self.book.values():
         print(i)

    def show_all_user(self):
        for i in self.user.values():
            User.show_user(i)

Library.recommend_books = recommend_books
Library.Book = Book
Library.add_books_from_csv = add_books_from_csv


lib = Library()

lib.add_books_from_csv()

user1 = User("John", "U100", [])
user2 = User("Mount", "U101", [])
user3 = User("James", "U102", [])
user4 = User("Yusra", "U103", [])
user5 = User("Sarah", "U104", [])
lib.add_user(user1)
lib.add_user(user2)
lib.add_user(user3)
lib.add_user(user4)
lib.add_user(user5)

lib.user_borrow("U100","100")
lib.user_borrow("U101","101")
lib.user_borrow("U102","102")
lib.user_borrow("U103","103")
lib.user_borrow("U104","101")
lib.user_borrow("U101","103")

lib.recommend_books("U101")
lib.recommend_books("U100")