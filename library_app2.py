from demo import Book
import csv
import os
def read_books_from_file(pathname):
    pass

def load_books(bookList, pathname):
    pass

def search_books(my_books_list, search_inp):
    pass

def borrow_book(my_books_list):
    pass

def find_book_by_isnb(my_books_list, ISBN):
    pass

def return_book(my_book_list):
    pass

def add_book(book_list):
    pass

def remove_book(my_books_list):
    pass

def print_books(my_books_list, pathname):
    pass

def save_books(my_books_list, pathname):
    pass

def main():
    book_list = []
    print("Starting the system...")
    pathname = input("Enter book catalog filename: ")
    while pathname != 'books.csv':
        print(f'File not found.') 
        pathname = input("Re-enter book catalog filename: ")
        break
    print("Book catalog has been loaded")
    book_list = load_books(book_list, pathname)
    
    
    
    MENU_OPT = {
    1: 'Search for books',
    2: 'Borrow a book',
    3: 'Return a book',
    0: 'Exit the system'
} 
    MENU_OPT2 =  {
    1: 'Search for books',
    2: 'Borrow a book',
    3: 'Return a book',
    4: 'Remove a book',
    5: 'Print all books',
    6: 'Exit the system',
    0: 'Exit the system'
} 
    
    menu_heading = "Reader's Guild Library - Main Menu"
    
    
    for key, value in MENU_OPT.items():
            print(f"{key}: {value}")
    choice = int(input("Enter your selection: "))
        
    
    while True:
    
        if choice == 0:
            break
        elif choice == 1:
            user_search = input("Which book are you searching for? ")
            search_books(book_list, user_search)
            print_books(menu_heading, MENU_OPT)
        elif choice == 2:
            borrow_book(book_list)
        elif choice == 3:
            return_book(book_list)
        elif choice == 4:
            add_book(book_list)
        elif choice == 5:
            remove_book(book_list)
        elif choice == 6:
            print_books(menu_heading, MENU_OPT2)
        elif choice == 2130:
            print(menu_heading)
            for key, value in MENU_OPT2.items():
               print(f"{key}: {value}")
            choice = int(input("Enter your selection: "))  
        else:
            print("Invalid choice. Please try again.")
    
    save_books(book_list, pathname)
    
if __name__ == "__main__":
    main()
