import numpy

# reading input file
filename = 'a_example.txt'
f = open(filename, "r")

line = f.readline().split(" ")

#
# read in input files
#
print(line)
B, L, D = int(line[0]), int(line[1]), int(line[2].strip())



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

