# Imagine yourself in a electronics store, buying a new camera.
# The store assistant sys, "This is a great camera, it has a 16-
# megapixel matrix", and you are frantically trying to remember
# what the word "matrix" means. Let's figure it out.

# The matrix of a 16 MP digital camera is a rectangular array of
# 4928 by 3264 photosensors, each representing a pixel. If you
# multiply these numbers, you will get 16,084,992 (about 16
# million) pixels.

# In fact, if you really are into buying a camera, you should know
# that the number of pixels is not the only thing that matters;
# their physical size is also important. A matrix with bigger pixels
# produces a better quality image.

# Okay, so you have bought that camera, and the information
# about your purchase has appeared in the accounting table of the
# store like this:

#           | July      | August        | September|
# Canon     | 8         | 21            | 9        |
# Nikon     | 5         | 2             | 11       |
# Sony      | 12        | 4             | 11       |
# Olympus   | 2         | 15            | 4        |

# this table, as well as the matrix with pixels, can be represented
# as a matrix (plural: matrices):
# A4,3 = [[8, 21, 9],
#         [5, 2, 11],
#         [12, 4, 11],
#         [2, 15, 4]]

# In general, a matrix is a rectangular array of elements arranged
# in rows and columns. The elements can be numbers, symbols,
# or expression. Below we will talk about numerical elements.

#                       Columns
#         Name
#               A4,3 = [[8, 21, 9],
#             |     |   [5, 2, 11],      Rows
#             |     |   [12, 4, 11],
#             |     |   [2, 15, 4]]
#             |     |            --
#         Rows, Columns                 Matrix
#                                       Element


# 1. Matrix Dimension
# The number of rows and columns defines the dimension of a
# matrix.

# For example, matrix A4,3 has 4 rows and 3
# columns, so the dimension of matrix A is 4 x 3 (read "four by
# three").

#   NOTE: The number of rows is followed by the number of
#   columns.

# More generally, an m x n matrix has m rows and n columns:

# Am,n = [[A1,1,     A1,2,   ...,   A1,n],
#         [A2,1,     A2,2,   ...,   A2,n],
#         [ |  ,      |  ,   ...,    |  ],
#         [Am,1,     Am,2,   ...,   Am,n]]

# 2. Vectors
# If a matrix has only one row D1,4 = (13   4   0   10) or more
# column U3,1 = [2, such matrices are called vectors (row
#                21,
#                6]
# vector or column vector). Example: the coordinates of a point K
# (7    0   -13) in the three-dimensional space is a matrix "one
# by three".

# 3. Matrix Elements
# Each element has its own position in the matrx. In matrix A, an
# element in row m and column n is represented by amn. In our
# electronics shop example a12 = 21 tells us that the
# Canon cameras were purchased 21 times in August (check the
# table above).


# A4,3 = [[8, 21, 9],  Row1
#         [5, 2, 11],
#         [12, 4, 11],
#         [2, 15, 4]]
#           Column 2

# The order of elements in the matrix is important. Imagine what
# would happen with our world if point P (4     3   -1) and point
# F (-1   3   4) occupied the same place?

# In computer graphics, matrices are used in such operations as
# translations, rotations, scaling, and more. These concepts are
# relevant to video game graphics. Understanding matrices is a
# basic necessity for programming 3D video games. Also the
# matrix which we mention above is real: computers can process
# photos preciesly because the images are presented as matrices
