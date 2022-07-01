#Library - operation
#1 issue
#2 Return
def star():
    for i in range(0,50):
        print("*",end=' ')
    print('\n')
books={1130:"Harry Potter",7654:"Moon Knight",5443:"Cinderella",8990:"Donald Duck",4665:"Garfield"}
#issuing the book
issued_book={}
key=int(input("Enter book id to issue book:"))
issue_b=books.pop(key)
issued_book[key]=issue_b
print("Book which is issued:",issued_book)
print("After issuing book of id "+str(key)+" Dictionary is:")
print(books)
star()

#Returning a book
print("After Returning book of id "+str(key)+" Dictionary is:")
books.update(issued_book)
print(books)
