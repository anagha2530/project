class Books:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"title:{self.title},author:{self.author} and isbn:{self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        print("Book",book.title,"is succesfully added")

    def view_books(self):
        if not self.books:
            print("not found")
        else:
            for i in self.books:
                print(i)

    def search_books(self,query):
        found_book = [book for book in self.books if (query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in book.isbn.lower())]
        if not found_book:
            print("book not found")
        else:
            for book in found_book:
                print(book)
    
def main():
    lib = Library()
    while True:
        print("Library menu")
        print("""
            1.Add Books
            2.View Books
            3.Search Books
            4.Exit
              """)
        ch = int(input("enter the choice(1,2,3,4): "))

        if ch == 1:
            title = input("enter the title of the book: ")
            author = input("enter the author of the book: ")
            isbn = input("enter the isbn: ")
            book = Books(title,author,isbn)
            lib.add_books(book)

        elif ch == 2:
            lib.view_books()

        elif ch == 3:
            query = input("enter the query(title,author,isbn): ")
            lib.search_books(query)

        elif ch == 4:
            print("exit from library application")
            break

        else:
            print("invalid choice")

if __name__=="__main__":
    main()