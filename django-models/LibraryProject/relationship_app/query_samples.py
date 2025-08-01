from .models import Author, Book, Librarian, Library

author_name = "ahmed"

try :
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print("Author not found.")


library_name = "Main Library"
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name} is {librarian.name}")
except Library.DoesNotExist:
    print("Library not found.")
except Librarian.DoesNotExist:
    print("Librarian not found.")    

try:
    librarian = library.librarian
    if librarian:
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    else:
        print(f"\nNo librarian assigned to {library.name}")
except Exception as e:
    print("Error retrieving librarian:", e)
