from book_recommendation_helper import sort_by_catagory, print_list, quick_sort, auto_complete

def inro():
    print("Welcome to the greatest book recommendation software! *")

def what_catagory():
    print("Please enter the first letter or first few letters of the Genre you are looking for and we'll let you know if we have books in that catagory ")
    while True:
        choice = input("Which Genre are you looking for? ").title()
        search_result = auto_complete(choice)
        if search_result != None:
            show_books = input("Would you like to see {genre}? yes or no ".format(genre = search_result)).title()
            if show_books == "Yes":
                break
