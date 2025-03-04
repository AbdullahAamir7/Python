class Library:
    def __init__(self,book_list,name) :
        self.listofBook=book_list
        self.name=name
        self.lendbook={}

    def Display_Book(self):
        print("We have the folloeing books in our library:")
        for book in self.listofBook:
            print(book)

    def lend_book(self,book,user):
        if book not in self.listofBook:
            print(f"Sorry we dont have {book} book.")
        
        elif book in self.lendbook:
            print(f"Sorry! {book} is already in used.")

        else:
            self.lend_book[book]=user
            print(f"You can Lend the {book} Book.")

    def add_Book(self,book):
            self.listofBook.appeand[book]
            print(f"Your has been added.")

    def return_book(self,book):
        if book not in self.listofBook:
            del self.lend_book[book]
            print("Thank YOu! to take our book service")
        else:
            print(f"{book} is not borrowed from us.")

if __name__ == "__main__":
    book=Library(["Python","Harry Poter","Rich Dad and Poor Dad","C++"],"Public Library")
    user_name=input("Wellcome to our Library! Enter Your name:")