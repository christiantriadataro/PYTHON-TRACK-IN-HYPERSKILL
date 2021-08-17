# Your task is to write a function print_book_info(title,
# author=None, year=None) that prints information about a book.
# Arguments author and year are optional, so be ready that they
# might equal None.

# You don't have to read the input. The information about a book will
# be passed to your function, and it should output it in the right
# format.

# See the examples below to understand the output format.

#     The knowledge of if-elif-else statements is expected in this
#     task. If it's not the case, please proceed to the next
#     challenge.

def print_book_info(title, author=None, year=None):
    if author is None and year is None:
        print(f'"{title}"')
    elif author is None:
        print(f'"{title}" was written in {year}')
    elif year is None:
        print(f'"{title}" was written by {author}')
    else:
        print(f'"{title}" was written by {author} in {year}')