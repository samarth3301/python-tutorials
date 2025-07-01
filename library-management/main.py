class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
    
    def add_book(self, name, author, pages):
        dict = {
            "name": name,
            "author": author,
            "pages": pages
        }
        self.books.append(dict)
        
    def remove_book(self, name):
        for book in self.books:
            if book["name"] == name:
                self.books.remove(book)
                
    def list_books(self):
        for books in self.books:
            print(books)
        
southExtentionLibrary = Library("UNIQUE LIBRARY")

def ask_book_details():
    name = input("Enter book name:")
    author = input("Enter author name:")
    pages = input("Enter total number of pages:")
    return name, author, pages


while True:
    print(f"===== {southExtentionLibrary.name} Management System =====")
    print("[1] : Add Book")
    print("[2] : Remove Book")
    print("[3] : Print Books")
    choice = int(input("Enter your operation :"))
    if (choice == 1):
        data = ask_book_details()
        southExtentionLibrary.add_book(*data)
    elif (choice==2):
        name = input("enter the book name:")
        southExtentionLibrary.remove_book(name)
    elif (choice == 3):
        southExtentionLibrary.list_books()
    if choice not in [1, 2, 3]:
        print("please enter valid data")