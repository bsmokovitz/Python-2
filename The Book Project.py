class Book:
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_date(self):
        return self.date

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Date: {self.date}"
    
class Fiction(Book):
    def __init__(self, title, author, date, genre):
        super().__init__(title, author, date)
        self.genre = genre

    def get_genre(self):
        return self.genre

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Date: {self.date}, Genre: {self.genre}"
    
class Text_book(Book):
    def __init__(self, title, author, date, pages, subject):
        super().__init__(title, author, date)
        self.pages = pages
        self.subject = subject

    def get_pages(self):
        return self.pages

    def get_subject(self):
        return self.subject

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Date: {self.date}, Pages: {self.pages}, Subject: {self.subject}"
    
class Picture(Fiction):
    def __init__(self, title, author, date, genre, illustrator):
        super().__init__(title, author, date, genre)
        self.illustrator = illustrator

    def get_illustrator(self):
        return self.illustrator

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Date: {self.date}, Genre: {self.genre}, Illustrator: {self.illustrator}"
    
class Library:
    def __init__(self):
        self.libr = []
        
    def add_book(self, book):
        self.libr.append(book)
        
    def print_books(self):
        for book in self.libr:
            print(book)

p1 = Picture("The Very Hungry Caterpillar", "Carle, Eric", 1967, "picture", "Carle, Eric")
b1 = Book("Python for Beginners", "Smith, Penelope", 1997)
f1 = Fiction("Pride and Prejudice", "Austen, Jane", 1813, "literature")
t1 = Text_book("Calculus for Engineers", "Smarty, Mildred", 1972, 1000, "math")
wrrl = Library()
wrrl.add_book(p1)
wrrl.add_book(b1)
wrrl.add_book(f1)
wrrl.add_book(t1)
wrrl.print_books()