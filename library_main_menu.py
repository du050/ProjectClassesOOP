# CPRG216 - OOP - Final Project
# Group 8: Grace Zilun, Maria Xavier, Armaandeep Singh
#
# This is a Library Management application, it enables user to interact with menu, to search books, to find book by isbn, to borrow/return book. It also allows Librarian to add/remove books, print catalog and more.

import os
import book

MENU_OPTIONS = {
    1: "Search for books",
    2: "Borrow a book",
    3: "Return a book",
    0: "Exit the system",
}


def load_books(file_name, book_list):
    """"""
    no_of_books = 0

    with open(file_name) as file:
        for line in file:
            isbn, title, author, genre, availability = line.strip().split(",")
            genre = int(genre)
            availability = bool(availability == "True")
            book_list.append(book.Book(isbn, title, author, genre, availability))
            no_of_books += 1
    print("Book catalog has been loaded.")
    return no_of_books


def print_header():
    print(
        "\n{:14s} {:25s} {:25s} {:20s} {:s}".format(
            "ISBN", "Title", "Author", "Genre", "Availability"
        )
    )
    print(
        "{:14s} {:25s} {:25s} {:20s} {:s}".format(
            "-" * 14, "-" * 25, "-" * 25, "-" * 20, "-" * 12
        )
    )


def print_menu():
    """"""
    print("\nReader's Guild Library - Main Menu")
    print("==================================")
    for index, option in MENU_OPTIONS.items():
        print(f"{index}. {option}")

    selection = int(input("Enter your selection: "))

    while selection not in MENU_OPTIONS:
        print("Invalid selection.")
        selection = int(input("Enter your selection: "))
    else:
        return selection
    

def print_librarian_menu():
    print("\nReader's Guild Library - Librarian Menu")
    print("========================================")
 

def search_books(book_list, search_str):
    """"""
    search_result_list = []

    while True:
        search_result_list.clear()
        for book in book_list:
            book_info = (
                book.get_isbn()
                + book.get_title()
                + book.get_author()
                + book.get_genre_name()
            )
            if search_str.lower() in book_info.lower():
                search_result_list.append(book)

        if search_result_list:
            print_header()
            for book in search_result_list:
                print(book)
            return
        else:
            print("No matching books found.")
            return

def find_book_by_isbn(book_list, isbn):
    """"""
    index = 0
    while index < len(book_list):
        if isbn == book_list[index].get_isbn():
            return index
        index += 1
    else:
        return -1
    

def borrow_book(book_list):
    """"""
    print("\n-- Borrow a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    index = find_book_by_isbn(book_list, isbn)
    
    if index != -1:
        current_book = book_list[index]
        if current_book.get_available():
            current_book.borrow_it()
            print(
                f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} successfully borrowed."
            )
            return
        else:
            print(
                f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} is not currently available."
            )
            return
    print("No book found with that ISBN.")


def return_book(book_list):
    """"""
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)
    if index != -1:
        current_book = book_list[index]
        if current_book.get_available():
            print("The book has already returned.")
            return
        else:
            current_book.return_it()
            print("Book returned")
            return
    print("No book found with that ISBN.")

def main():
    """"""

    book_list = []  # initiate empty list
    print("Starting the system ... ")
    # file_name = input("enter book catalog filename: ")
    file_name = "books.csv"
    load_books(file_name, book_list)

    while True:
        
        selection = print_menu()  # return user's valid selection

        match selection:
            case 1:
                print("\n-- Serach for books --")
                search_str = input("Enter search value: ")
                search_books(book_list, search_str)
            case 2:
                borrow_book(book_list)
            case 3:
                return_book(book_list)
            case 0:
                print("Thank you.")
                break
            case _:
                print("Invalid input.")
 



# call main() function
if __name__ == "__main__":
    main()
