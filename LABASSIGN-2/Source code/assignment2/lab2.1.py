dictionary = {"harrypotter":50,"blackpanther":30,"avengers":20,"supergirl":40}
minim = int(input("Enter the minimum price range : "))
maxim = int(input("Enter the maximum price range : "))
bookslist = []
for price in range(minim,maxim+1):
    for bookname in dictionary:
        if dictionary[bookname] == price:
            bookslist.append(bookname)
print(" purchased your books are : " , bookslist)