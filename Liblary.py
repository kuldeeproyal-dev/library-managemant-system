def main():
    Books ={}
    load_books_data()
    show_menu()
    option = int(input("Select your option"))
    if option == 1:
        take_book()
    elif option == 2:
        return_book()
    elif option == 3:
        search_available_books()
    elif option == 4:
        display_authors()
    elif option == 5:
        display_categories()
    elif option == 6:
        donate_book()
    elif option == 7:
        print ("Exiting the Application")
        exit()
    else:
        print("Invalid option. Please try again.")
        return main()
    
def load_books_data():
    # This function would load book data from a file or database
    # For now, we will just return an empty dictionary
    pass

def show_menu():
    print ("\n---Libary Menu---")
    print ("1. Take a book")
    print ("2. Return a book")
    print ("3. Search book availablity")
    print ("4. Search by author")
    print ("5. Search by categories")
    print ("6. Donate a book")
    print ("7. Exit")

def take_book():
    #this function will allow a user to take a book from the library
    pass

def return_book():
    #this function will allow a user to return a book to the library
    pass

def search_available_books():
    #this function will display all available books in the library
    pass

def display_authors():
    #this function will display all authors of the books in the library
    pass

def display_categories():
    #this function will display all categories of books in the library
    pass

def donate_book():
    #this function will allow a user to donate a book to the library
    pass