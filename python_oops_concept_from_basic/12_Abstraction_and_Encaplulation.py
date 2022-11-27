#Abstraction_and_Encaplulation

class Library:
    def __init__(self,books) :
        self.books=books

    def listbooks(self):
        print("\t\tAvilable Books")
        for book in self.books:
            print(book)


    def borrow_books (self,borrow_books):
        if borrow_books in self.books:
            print("Get your Book now")
            self.books.remove(borrow_books)

        else:
            print("Book not Avilable")

    def recived_book(self,recived_book):
        print("you have returned the book")
        self.books.append(recived_book)            
books=["Python","java","c++"]
o=Library(books)
msg="""
1.Display Book
2.Borrow Book
3.Return Book"""
while True:
    print(msg)
    ch=int(input("Enter the number : "))
    if ch==1:
        o.listbooks()
    elif ch==2:
        book=input("Enter Book Name To Borrow : ")
        o.borrow_books(book)
    elif ch==3:
        book=input ("Enter Book Name To Return : ")
        o.recived_book(book)    
    else    :
        print("Thank You come again")
        quit()