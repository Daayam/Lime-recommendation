from book_recommendation_data import book_catagories, books

def auto_complete(user_input):
    if user_input in book_catagories:
        return user_input
    return None

def sort_by_catagory(desired_catagory = None): # fucntion to sort books by a given catagory
    books_copy = [ [title, attributes] for title, attributes in books.items()] # add all the books to a 2-D list
    books_by_catagory = {} # dictionary used to store books as values and catagories as their respective keys

    if desired_catagory == "All": # adds all books together regardless of catagory
        books_list = [book[0] for book in books_copy]
        sorted_list = ["All Books", books_list]
    
    elif desired_catagory == None: # includes all catagories with their respective books
        for catagory in book_catagories:        
            books_by_catagory[catagory] = [book[0] for book in books_copy if book[1][1] == catagory] # adding books by catagory to the dictionary
            sorted_list = [[catagory, titles] for catagory, titles in books_by_catagory.items()]
    
    else: # includes only the desired catagory and the books in it
        books_by_catagory[desired_catagory] = [book[0] for book in books_copy if book[1][1] == desired_catagory] # adding only the books in the desired catagory
        sorted_list = [desired_catagory, books_by_catagory[desired_catagory]]

    return sorted_list

def print_list(list_to_print): # function to aesthetically print a list of books

    if len(list_to_print) > 2: # if the list has multiple catagories
        for catagory in list_to_print: # loop through the different catagories
            print("\n" + catagory[0]) # print each catagory
            print("_______________________________________________\n\n")
            for book in catagory[1]:
                print("{Title} \nBy {Author} \n{Year} \n{Description} \n".format(Title = book, Author = books[book][0], Year = "Year Needed", Description = books[book][2])) # uses the title (key) of the book to access the details (values) of that book from the books dictionary
                print("///////////////////////////////////////////\n")

    else: # if the list has one catagory
        print("\n" + list_to_print[0]) # print catagory
        print("_______________________________________________\n\n")
        for book in list_to_print[1]: # loops through each book in the chosen catagory
            print("{Title} \nBy {Author} \n{Year} \n{Description} \n".format(Title = book, Author = books[book][0], Year = "Year Needed", Description = books[book][2]))
            print("///////////////////////////////////////////\n")

def quick_sort(input_list, sort_by):
    middle = len(input_list)//2 # if sorting by recommended, the smallest value will always be 1, and the largest will always be equal to the number of elements.
    return input_list
   
x = sort_by_catagory()
print(x)
print_list(x)
