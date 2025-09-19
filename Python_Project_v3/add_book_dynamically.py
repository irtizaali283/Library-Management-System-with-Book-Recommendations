import pandas as pd
from Books import Book

def add_books_from_csv(self):
    df = pd.read_csv("Recommendation_of_Books.csv")
    for index, row in df.iterrows():
        genres = [g.strip() for g in row["Genres"].split(",")]
        book = Book(
            title=str(row["Title"]).strip(),
            author=str(row["Author"]).strip(),
            isbn=str(row["ISBN"]).strip(),
            publication_year=int(row["Publication Year"]),
            total_copies=int(row["Total Copies"]),
            available_copies=int(row["Available Copies"]),
            genres=genres
        )
        self.add_book(book)