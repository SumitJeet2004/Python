#Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped! in python
class Library:
    def __init__(self):
        self.books = []  # List to store the books
        self.no_of_books = 0  # Number of books in the library
    
    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
    
    def get_no_of_books(self):
        return self.no_of_books
    
    def print_books(self):
        if self.no_of_books == 0:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

# Function to demonstrate the Library class
def main():
    # Create an instance of Library
    my_library = Library()
    
    # Add some books to the library
    my_library.add_book("The Great Gatsby")
    my_library.add_book("1984")
    my_library.add_book("To Kill a Mockingbird")
    
    # Print all books in the library
    my_library.print_books()
    
    # Get and print the number of books in the library
    print(f"Number of books in the library: {my_library.get_no_of_books()}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
