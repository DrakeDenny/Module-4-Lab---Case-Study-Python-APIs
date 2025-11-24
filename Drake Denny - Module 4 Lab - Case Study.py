
class Book:
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f"{self.id}: {self.book_name} by {self.author} ({self.publisher})"


# Our in-memory "database"
books = []



# CREATE
def create_book(id, book_name, author, publisher):
    new_book = Book(id, book_name, author, publisher)
    books.append(new_book)
    return new_book


# READ ALL
def read_books():
    return books


# READ BY ID
def read_book(id):
    for book in books:
        if book.id == id:
            return book
    return None


# UPDATE
def update_book(id, book_name=None, author=None, publisher=None):
    book = read_book(id)
    if book:
        if book_name:
            book.book_name = book_name
        if author:
            book.author = author
        if publisher:
            book.publisher = publisher
        return book
    else:
        return None


# DELETE
def delete_book(id):
    global books
    books = [book for book in books if book.id != id]


if __name__ == "__main__":
    # Create books
    print("Creating books...")
    create_book(1, "The Old Breed", "E.B. Sledge", "Presidio Press")
    create_book(2, "Lone Survivor", "Marcus Luttrell", "Little, Brown")

    # Read all books
    print("\nAll books:")
    for b in read_books():
        print(b)

    # Read one book
    print("\nReading book with ID 1:")
    print(read_book(1))

    # Update book
    print("\nUpdating book ID 1...")
    update_book(1, author="E.B. Sledge (Updated)")
    print(read_book(1))

    # Delete a book
    print("\nDeleting book ID 2...")
    delete_book(2)

    # Read all books again
    print("\nBooks after deletion:")
    for b in read_books():
        print(b)
