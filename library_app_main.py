# CPRG216 - OOP - Final Project
# Group 8: Grace Zilun, Maria Xavier, Armaandeep Singh
#
# This is a Library Management application, it enables user to interact with menu, to search books, to find book by isbn, to borrow/return book. It also allows Librarian to add/remove books, print catalog and also save the updates to file and exit the system.

import os
import book

def load_books(file_name, book_list):
    """
    Receives file_name and empty book_list
    Iterate through each line in the file, create Book objects and add them onto the list
    """
    with open(file_name) as file:
        for line in file:  # Iterated through each line in the file

            # Parsing the attribute values into separate variables
            isbn, title, author, genre, availability = line.strip().split(",")

            # Convert the genre to an integer to match the expected data type
            genre = int(genre)

            # Convert the availability string to a boolean to match the data type
            availability = bool(availability == "True")

            # Create a Book object using the parsed attributes, and append each book object to book_list
            book_list.append(book.Book(isbn, title, author, genre, availability))

            # Increment the count of books

    print("Book catalog has been loaded.")


def print_header():
    """Print the formatted catalog header"""
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


def print_menu(menu_heading, menu_option):
    """
    Receive menu heading and menu options
    Print main menu, ask user to input valid selection
    """
    print(menu_heading)

    # Ask user to enter selection until a valid input is entered
    for index, option in menu_option.items():
        if index != "2130":  # Not displaying the hidden option '2130'
            print(f"{index}. {option}")

    # Ask user to input selection until a valid selection is entered
    selection = input("Enter your selection: ")
    while selection not in menu_option:
        print("Invalid option.")
        selection = input("Enter your selection: ")
    else:
        return selection


def search_books(book_list, search_str):
    """
    Receives book_list and search_string, iterates through the book_list
    Append the matched book to the search_result_list
    """
    search_result_list = []  # Initiate empty search result list

    for book in book_list:
        # Create a string called book_info, that concatenates ISBN, title, author, and genre name
        book_info = (
            book.get_isbn()
            + book.get_title()
            + book.get_author()
            + book.get_genre_name()
        )
        # Perform a case-insensitive search
        if search_str.lower() in book_info.lower():
            search_result_list.append(book)

    # Pass the search_result_list into function print_book
    print_book(search_result_list)


def borrow_book(book_list):
    """
    Receives the book_list, ask user to input ISBN and call find_book_by_isbn,
    If an index of a matched book is returned and the book is available, invokes the book's borrow_it() method
    """
    print("\n-- Borrow a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    # Get index from find_book_by_isbn() function
    index = find_book_by_isbn(book_list, isbn)

    # If returned index is -1, print message 'No book found with the ISBN.'
    if index != -1:
        # Initiate the reference object current_book
        current_book = book_list[index]

        # Invoke current_book's get_available() method
        if current_book.get_available():
            # If availability is True(available), invoke borrow_it() method, set the availability to False
            current_book.borrow_it()
            print(
                f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} successfully borrowed."
            )
            return
        # If availability is False(not available), print the message
        else:
            print(
                f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} is not currently available."
            )
            return
    print("No book found with that ISBN.")


def find_book_by_isbn(book_list, isbn):
    """
    Receives book_list and ISBN
    Return the book index when the isbn is matched, return -1 when no isbn matched
    """
    index = 0  # Initiate a variable index

    # Iterates through the list and comparing each book's isbn
    while index < len(book_list):

        if isbn == book_list[index].get_isbn():
            return index  # Return index if isbn is matched
        index += 1  # Index increment

    else:
        return -1  # Return -1 if no isbn is matched


def return_book(book_list):
    """
    Receives the book_list, inputs an ISBN from user and call find_book_by_isbn()
    If an index to a matching book is returned and the book is currently borrowed, invoke the book's return_it() method
    """
    print("\n-- Return a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    # Get index from find_book_by_isbn()
    index = find_book_by_isbn(book_list, isbn)

    # If the book with the entered isbn is found, check the availability
    if index != -1:
        # Initiate a reference object current_book
        current_book = book_list[index]

        # Invoke the get_available() method, if it is available, print the message
        if current_book.get_available():
            print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} is not currently borrowed.")
            return
        # If it is not available, invoke the return_it() method, set availability to True
        else:
            current_book.return_it()
            print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} successfully returned.")
            return
    # If no book is found, print error message
    print("No book found with that ISBN.")


def add_book(book_list):
    """
    Receives book list, ask user to iput ISBN, title, author and genre name, validate the genre name Creat a new instance of Book and appends it to the list
    """
    # Access to the static class constant defiend within the 'Book' class, assign it to a variable 'genre_option'
    genre_option = book.Book.GENRE_OPTION

    # Prompt the user to input the book's ISBN, title, author, and genre name
    print("\n-- Add a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    genre_name = input("Enter genre: ")

    # Iterates through the values of genre_option dictionary, ask user to re-enter until a valid genre name is provided
    while genre_name not in genre_option.values():
        print(f"Invalid genre. Choices are: {', '.join(genre_option.values())}")
        genre_name = input("Enter genre: ")

    # Find the corresponding key (genre index) for the entered genre name in the dictionary
    # Assign the key to the varible 'genre_index'
    for key, value in genre_option.items():
        if value == genre_name:
            genre_index = key
            break

    # Create a new instance of the 'Book' class with the provided attributes, set the 'available' to True by default
    # Append the newly created book object to the book_list
    book_list.append(book.Book(isbn, title, author, genre_index, available=True))
    print(f"'{title}' with ISBN {isbn} successfully added.")


def remove_book(book_list):
    """
    Receives book_list, inputs ISBN from user and call find_book_by_isbn()
    Remove the book from the list if the book is found, otherwise displays the 'not found' message
    """
    print("\n-- Remove a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, isbn)

    if index != -1:
        print(
            f"'{book_list[index].get_title()}' with ISBN {book_list[index].get_isbn()} successfully removed."
        )
        book_list.pop(index)
    else:
        print("No book found with that ISBN.")


def print_book(book_list):
    """
    Receives the search_result_list from search_book() function
    Or, called upon menu selection '6. Print catalog', receives the full book_list
    """
    print("\n-- Print book catalog --")

    # if the book_list is not empty, print header and each book
    if book_list:
        print_header()
        for book in book_list:
            print(book)
        return
    # if the book_list is empty, print the message
    else:
        print("No matching books found.")
        return


def save_books(file_name, book_list):
    """
    Receives book_list and file name, iterates over the list, format each book's attribute values into a comma-separated string
    Write each formatted string as a sperate line to the file
    """
    # Initialize an empty string to accumulate book info
    formatted_book = ""

    # Iterate through each book in the book_list
    for book in book_list:
        # Format the book's attributes (ISBN, title, author, genre, availability)
        # Append the formatted string to 'formatted_book' followed by new line char \n
        formatted_book += f"{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_available()}\n"

    # Open the file in write mode, and write the accumulated string to the file
    with open(file_name, "w") as file:
        file.write(formatted_book)


def main():
    """
    Main function to run the Reader's Guild Library system.
    Initializes the menu, loads the book catalog, and handles user interactions.
    """
    # Initiate the default menu options as dictionary
    menu_option = {
        "1": "Search for books",
        "2": "Borrow a book",
        "3": "Return a book",
        "0": "Exit the system",
        "2130": "",  # Key for librarian menu access, initially with an empty value
    }

    # Initiate the default heading for main menu
    menu_heading = "\nReader's Guild Library - Main Menu\n" + "=" * 34

    # initiate an empty book list
    book_list = []
    print("\nStarting the system ... ")
    file_name = input("Enter book catalog filename: ")

    # Ask user input for file name until a valid file name is entered
    while file_name != "books.csv":
        file_name = input("File not found. Re-enter book catalog File name: ")
        break

    # Load the book catalog from the books.csv file into the book_list
    load_books(file_name, book_list)

    # Loop to handle user interactions based on menu selections
    while True:
        # Display the menue and get user's valid selection
        selection = print_menu(menu_heading, menu_option)

        # Handle menu options using match-case
        match selection:

            case "1":
                # Search for books based on user input
                print("\n-- Serach for books --")
                search_str = input("Enter search value: ")
                search_books(book_list, search_str)

            case "2":
                # Borrow a book from the library
                borrow_book(book_list)

            case "3":
                # Return a borrowed book
                return_book(book_list)

            case "4":
                # Add a new book to the catalog
                add_book(book_list)

            case "5":
                # Remove a book from the catalog
                remove_book(book_list)

            case "6":
                # Print the entire book catalog
                print_book(book_list)

            case "0":
                # Save the book catalog and exit the system
                save_books(file_name, book_list)
                print("\n-- Exit the system --")
                print("Book catalog has been saved.")
                print("Good Bye!")
                break  # Exit the loop and terminate program

            case "2130":
                # Switch to the Librarian Menu with addtinoal options

                # Modify the menu_heading with Librarian Menu
                menu_heading = "\nReader's Guild Library - Librarian Menu\n" + "=" * 40

                # Use pop() method of dictionary to remove the 'Exit' option temporarily
                menu_option.pop("0")

                # Use update() method to add new options to the menu_option dictionary
                menu_option.update(
                    {
                        "4": "Add a book",
                        "5": "Remove a book",
                        "6": "Print catalog",
                        "0": "Exit the system",  # Re-add the 'Exit' option at the end
                    }
                )


# call main() function
if __name__ == "__main__":
    main()
