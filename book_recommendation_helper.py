from book_recommendation_data import book_catagories, books

def sort_by_catagory(desired_catagory = None):
    books_copy = [ [title, attributes] for title, attributes in books.items()]
    books_by_catagory = {}

    if desired_catagory == "All":
        books_list = [book[0] for book in books_copy]
        sorted_list = ["All Books", books_list]
    
    elif desired_catagory == None:
        for catagory in book_catagories:        
            books_by_catagory[catagory] = [book[0] for book in books_copy if book[1][1] == catagory]
            sorted_list = [[catagory, titles] for catagory, titles in books_by_catagory.items()]
    
    else:
        books_by_catagory[desired_catagory] = [book[0] for book in books_copy if book[1][1] == desired_catagory]
        sorted_list = [desired_catagory, books_by_catagory[desired_catagory]]

    return sorted_list

def quick_sort(input_list, sort_by):
    pass
    
print(sort_by_catagory("All"))