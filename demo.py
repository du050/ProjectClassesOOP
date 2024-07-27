class Book:
    def __init__(self, isbn, title, author, genre, avaliable):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.avaliable = bool(avaliable)
    
    def get_isbn(self):
        return self.isbn
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    
    def get_avaliable(self):
        return self.avaliable
    
    GENRES_DICT = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children’s Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }
    
    def get_genre_name(self, index: int) -> str:
        return self.GENRES_DICT.get(index, "Invalid index")

    def get_availability(self):
        if self.avaliable == True:
            return "Available"
        elif self.avaliable == False:
            return "Borrowed"
    
    def set_isbn(self, isbn: str):
        self.isbn = isbn
    
    def set_title(self, title: str):
        self.title = title
    
    def set_author(self, author: str):
        self.author = author
    
    def set_genre(self, genre: int):
        self.genre = genre
    