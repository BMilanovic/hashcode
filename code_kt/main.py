#import numpy
import Book

# reading input file
input_filename = 'a_example.txt'
input_file = open(input_filename, "r")
total_books, total_libraries, total_days = input_file.readline().split()
total_books, total_libraries, total_days = int(total_books) , int(total_libraries), int(total_days)

book_scores = input_file.readline().split()
index = 0
all_books = []
for book_score in book_scores:
    book = Book.Book(index, int(book_score))
    all_books.append(book)
    index += 1

#while


#line = f.readline()

#
# read in input files
#

#B, L, D = int(line[0]), int(line[1]), int(line[2])



# Class Book
# Book parameters
# ID, score

# Class Library
# Lib
# num books
# num days
# ship days
# [book ids]

######################

# 1. Signup Queue

# 2. Library Selection System (LSS)
# - selection based on registry score - penalty score
# - update (2x, 1x similarity matrix (Boris), 1x registry (Khaled))

# 3. Registry (key performance indicators) (expensive)
#   Static
#   Dynamic, per-day and for-all-days part
#   => Scoring

# Similarity Matrix (cheap)
#   => penalty for the LSS
