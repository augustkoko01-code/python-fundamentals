# Class: BookShelf
class BookShelf:

    # Constructor
    # Creates a new bookshelf object.
    # The default capacity is 10 books.
    def __init__(self, capacity=10):
        self.capacity = capacity   # Store the maximum number of books.
        self.size = 0              # The shelf starts with 0 books.

    # Returns the bookshelf as book emojis.
    # The number of emojis depends on self.size.
    def __str__(self):
        return "📘" * self.size

    # Adds n books to the shelf.
    def add_books(self, n):
        self.size += n

    # Removes n books from the shelf.
    def remove_books(self, n):
        self.size -= n


# Create a bookshelf with a capacity of 5 books.
shelf = BookShelf(5)

# Print the bookshelf.
# No books yet, so nothing is shown.
print(shelf)

# Add 3 books to the shelf.
shelf.add_books(3)

# Print the bookshelf.
# Shows 3 book emojis.
print(shelf)

# Remove 1 book from the shelf.
shelf.remove_books(1)

# Print the bookshelf.
# Shows 2 book emojis.
print(shelf)

# Print the maximum number of books the shelf can hold.
print(shelf.capacity)

# Print the current number of books on the shelf.
print(shelf.size)