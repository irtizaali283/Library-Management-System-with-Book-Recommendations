class Book:
    def __init__(self, title, author, isbn, publication_year, total_copies, available_copies,genres):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.genres = genres


    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        return f"Title: {self.title} , Author: {self.author} , ISBN: {self.isbn} , Available copies: {self.available_copies} , Total copies: {self.total_copies} , Genres: {self.genres}"