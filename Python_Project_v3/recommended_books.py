import pandas as pd
def recommend_books(self, user_id):
    if user_id not in self.user:
        print(f"User {user_id} not found.")
        return

    user = self.user[user_id]

    if not user.borrowed_books:
        print(f"User {user_id} has not borrowed any books.")
        return

    df=pd.read_csv("Recommendation_of_Books.csv")
    df["ISBN"] = df["ISBN"].astype(str).str.strip()
    df["Genres"] = df["Genres"].apply(lambda x :[g.strip() for g in x.split(",")])

    borrowed_books = [str(isbn) for isbn in user.borrowed_books]
    borrowed_genres = []

    for isbn in borrowed_books:
        book_row = df[df["ISBN"] == isbn]
        if not book_row.empty:
            borrowed_genres.extend(book_row.iloc[0]['Genres'])

    borrowed_genres = set(borrowed_genres)

    recommendations = df[~df["ISBN"].isin(borrowed_books)]
    recommendation = recommendations[recommendations["Genres"].apply(
        lambda g: any(genre in borrowed_genres for genre in g)
    )]

    if recommendation.empty:
        print("No recommendations found")
    else:
        print(f"\nRecommendations for {user.name}:")
        print(recommendation[["Title", "Genres"]].to_string(index=False))