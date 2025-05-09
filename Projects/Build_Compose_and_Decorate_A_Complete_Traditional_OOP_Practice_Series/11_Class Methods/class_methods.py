class Book:
    total_books = 0   # Class variable shared by all instances

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()   # Call class method when a book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1   # cls refers to the class


# Create objects
book1 = Book("The Reluctant Fundamentalist", 'Mohsin Hamid')
book2 = Book("In the Line of Fire", "Pervez Musharraf")

print(f"Total Books: {Book.total_books}")