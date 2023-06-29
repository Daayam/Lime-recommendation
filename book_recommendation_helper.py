from book_recommendation_data import book_catagories, books

def sort_by_catagory():
    books_copy = [ [title, attributes] for title, attributes in books.items()]
    books_by_catagory = {}
    
    for catagory in book_catagories:        
        books_by_catagory[catagory] = [book[0] for book in books_copy if book[1][1] == catagory]
        
    return books_by_catagory.items()

print(sort_by_catagory())