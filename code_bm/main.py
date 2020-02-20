#import numpy
import Book
import Library
import Registry
import LSS

# reading input file
#input_filename = 'a_example.txt'
#input_filename = 'b_read_on.txt'
#input_filename = 'c_incunabula.txt'
#input_filename = 'd_tough_choices.txt'
#input_filename = 'e_so_many_books.txt'
#input_filename = 'f_libraries_of_the_world.txt'
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


lib_index = 0
line2 = line1 = "some line"
all_libraries = []
while True:
    line1 = input_file.readline()
    line2 = input_file.readline() if line1 else None

    if not line1 or not line2:
        break
    lib_books_indices = [int(i) for i in line2.split()]
    lib_books = [all_books[i] for i in lib_books_indices]
    number_of_books, signup_days, books_per_day = line1.split()
    number_of_books, signup_days, books_per_day = int(number_of_books), int(signup_days), int(books_per_day)

    lib = Library.Library(lib_index, signup_days, books_per_day, number_of_books, lib_books)
    all_libraries.append(lib)

    lib_index += 1


#print(all_libraries)
#print(all_libraries[0].books)

reg = Registry.Registry(all_libraries)
reg.calculate()

lss = LSS.LSS(reg)
# lss.build_signup_queue()
result = lss.build_final_result()


output_file_path = input_filename.replace('.txt', '_submission.txt')
output_file = open(output_file_path, "w")
output_file.write(str(len(result))+'\n')
for lib_with_books in result:
    output_file.write(str(lib_with_books[0].id) + ' ' + str(len(lib_with_books[1]))+'\n')
    output_file.write(' '.join([str(book.id) for book in lib_with_books[1]])+ '\n')
output_file.close()

#output_lines = [
#    len(lss.signup_queue())


#    str(len(chosen_pizzas)),
#     '\n',
#    ' '.join(str(pizza) for pizza in sorted(chosen_pizzas))
#]
#output_file.writelines(output_lines)


#output_file.close()
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
