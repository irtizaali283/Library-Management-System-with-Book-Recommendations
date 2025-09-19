# Library-Management-System-with-Book-Recommendations
Project Overview  This is a Python-based Library Management System that allows managing books and users, borrowing/returning books, and recommending books based on previously borrowed books. The system uses CSV files to store book information and the Pandas library for data handling.

#Features

1.Library Management
.Add books to the library
.Add users to the library
.Borrow and return books

2.Book Recommendation System
.Suggests books to users based on genres of books they have already borrowed.
.Uses a CSV file (Recommendation_of_Books.csv) containing book information.

3.Dynamic CSV Book Import
.Automatically reads book details from CSV and adds them to the library.

File Structure:

main.py → Main library management system with classes: Library, User, Book.
Books.py → Book class definition.
recommended_books.py → recommend_books method to generate recommendations.
add_book_dynamically.py → Reads books from CSV and adds them to the library.
Recommendation_of_Books.csv → CSV file containing all books and their details.
