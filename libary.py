class Book:

    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.is_borrowed = False

    def borrow(self):
         self.is_borrowed = True
         print("You have offically bowwored a book from the library. This is your certificate")

    def return_book(self):
        self.is_borrowed = False



book1 = Book("Time to rise", "Surabhi Mathur", False)
book2 = Book("Smile", "Raina Tegilmer", False)
book3 = Book("Harry Potter", "jk.rowling", False)

for i in (book1,book2, book3):
    i.title()
    i.author()
    i.is_borrowed()