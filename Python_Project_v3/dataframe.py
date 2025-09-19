import pandas as pd

data= {
    "ISBN": ["100","101","102","103"],
    "Title": ["DUNE","Foundation","Pride and Prejudice","The Martian"],
    "Author": ["Frank Herbert","Isaac Asimov","Jane Austen","Andy Weir"],
    "Genres": ["Science Fiction,Adventure","Science Fiction,Space Opera","Romance,Classic","Science Fiction,Adventure"],
    "Total Copies": [5,3,4,3],
    "Available Copies": [5,3,4,3],
    "Publication Year": [1965,1951,1813,2011]
}

df = pd.DataFrame(data)
df.to_csv("Recommendation_of_Books.csv",index=False)




