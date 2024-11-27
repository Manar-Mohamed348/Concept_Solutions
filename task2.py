print("enter done if you enterd the last book")
print("enter the books")
books={}
unique_titles=set()
while True:
   input_books=input()
   if(input_books.lower()=='done'):
    break
   title,days=input_books.split("-")
   if title.isnumeric():
     print("enter a vaild name")
     continue
   
   if not (days.isnumeric()):
     print("enter a vaild number")
     continue
   
   
   days=int(days)
   books[title] = days 
   unique_titles.add(title)
  
# for title in unique_titles:
#    print(title)
   most_borrowed_book=set()
print("the most borrowed book" )
maxi=max(books.values())
for title,days in books.items():
  
 if(days==maxi):
  most_borrowed_book.add(title)
  
print(most_borrowed_book)
  #################################
least_borrowed_book=set()
print("the least borrowed book" )
mini=min(books.values())
for title,days in books.items():
  
 if(days==mini):
  least_borrowed_book.add(title)
  
print(least_borrowed_book)
 #################################
averge=round(sum(books.values()) / len(books),2)
print("the average borrowing time = ", averge)
print("sort",sorted(books.values(),reverse=False))
