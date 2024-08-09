
class Book:
    # initiate a dictonary as staticclass constant 
    GENRE_NAME = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry",
    }

    def __init__(self, isbn, title, author, genre, available=True):
        self.__isbn = isbn
        self.__title = title
        self.__author = author 
        self.__genre = genre # genre is integer
        self.__available = available # available is boolean
 
    # Getters for isbn, title, author, genre and availability
    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
    def get_available(self):
        return self.__available
    
    # method get_genre_name()
    def get_genre_name(self):
        return Book.GENRE_NAME[self.__genre] # map index to genre name
       
    # setters for isbn, title, author and genre
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
    def set_title(self, new_title):
        self.__title = new_title
    def set_author(self, new_author):
        self.__author = new_author
    def set_genre(self, genre_value):
        self.__genre = genre_value

    # method get_availability()
    def get_availability(self):
        if self.__available:
            return "Available"
        else:
            return "Borrowed"

    # method borrow_it()
    def borrow_it(self):
        self.__available = False

    # method return_it()
    def return_it(self):
        self.__available = True

    # method __str__()
    def __str__(self):
        return f"{self.__isbn:14s} {self.__title:25s} {self.__author:25s} {self.get_genre_name():20s} {self.get_availability():s}"
    
    
