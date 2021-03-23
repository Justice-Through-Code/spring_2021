'''
Object-oriented book challenge! 

Your challenge for today is to complete the fill out the missing parts of the Booklist class in oop_book_challenge.py
Then, test each method for the class Booklist!

Hint: all methods for the Booklist class go in the oop_book_challenge.py script
This class and the methods are already imported in this script -- test them here!
'''

# import the Booklist class and corresponding methods
from book_class_solution import *


'''
PART #1. 
Set up the initialization function for class Booklist()
The function should initialize just 1 attribute, called 'books', as an empty list
No parameters needed, other than self

Then, create an object of class Booklist called 'my_library' in this script.
Finally, print the books attribute of my_library -- it should be an empty list
Also, print out the type of my_library to see what you get :) 

'''
print('PART 1\n')

my_library = Booklist()
print(my_library.books)
print(type(my_library))

'''
Part #2: 
Define the add() method to add a book to your Booklist
-The method should take 2 parameters other than self, both strings -- 'title', and 'author'
-The method should make a book variable as a dictionary with two key/value pairs for title/author
-Then, the method should append this book to books attribute of the the Booklist object  - i.e. self.books.append(book)

Once you have finished the method, add the following books to your booklist:
Just Mercy - Bryan Stevenson
The New Jim Crow - Michelle Alexander
The Truths We Hold - Kamala Harris
My Grandmother's Hands - Resmaa Menakem

Finally, print the books attribute of my_library to make sure your books have been added!
'''
print('\nPart 2\n')

# add the books
my_library.add(title = 'Just Mercy', author = 'Bryan Stevenson')
my_library.add(title = 'The New Jim Crow', author = 'Michelle Alexander')
my_library.add(title = 'The Truths We Hold', author = 'Kamala Harris')
my_library.add(title = "My Grandmother's Hands", author = 'Resmaa Menakem')

# print out the books
print(my_library.books)



'''
Part #3: 
Define the count_books() method to get the number of books in your Booklist
-the method only needs the self parameter
-the method should return an integer that is the length of the list stored in the books attribute

Once you have finished the method, count the books in my_library and print out the result
'''
print('\nPart 3\n')

# count the books
num_books = my_library.count_books()

# print the result
print(num_books)


'''
Part #4: 
Define the remove_title() method which will remove a book by its title from a Booklist
-the method should take the self parameter, plus an additional paramter 'title' (a string for the title of the book to remove)
-the method should remove any books matching the input title from the Booklist
-it does not need to return anything

Once you have finished the method, remove 'Just Mercy' from my_library
Then, print out the books attribute to make sure that book is gone
'''

print('\nPart 4\n')
my_library.remove_title('Just Mercy')
print(my_library.books)


'''
Part #5:
Instantiate another Booklist class called nyt_bestsellers
Then, add 2 books of your choice from the New York Times best sellers lists to nyt_bestsellers using the .add() method
You can find NYT books here: https://www.nytimes.com/books/best-sellers/

Then, print out the books attribute of nyt_bestsellers
'''

print('\nPart 5\n')

# initialize new Booklist object
nyt_bestsellers = Booklist()

# add books
nyt_bestsellers.add('A time for mercy', 'John Grisham')
nyt_bestsellers.add('The return', 'Nicholas Sparks')

# print out
print(nyt_bestsellers.books)


'''
BONUS Part #6:
Define a display_titles() method to display all the titles of the books in a Booklist
The titles should be displayed in alphabetical order!
-The method requires no parameters other than self

HINT: there's a quick way to sort a list in alphabetical order

Once you have completed this method, test it out on both my_library and nyt_bestsellers
'''

print('\nBONUS Part 6\n')

# display titles for both
my_library.display_titles()
nyt_bestsellers.display_titles()
