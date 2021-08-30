# When Anton finished reading "War and Peace", he decided to
# find out the number of specific words used in the book.

# Help Anton write a simplified version of such a program, that
# will be capable of counting the words separated with space, and
# print the statistics.

# The program must prompt a user for 1 line and print out each
# unique word with the number of its usages in the line in the
# following format "word amount" (case insensitive!), The word
# order does not matter, each word must be printed only once.
# dictionary = {key: value for element in iterable}
# plantes_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in
#                         planets_diameter_km.items() if value > 10_000}
#words = input().lower().split()
#count = {}
#for i in words:
#    if i in count:
#        count.update({i.lower(): 2})
#    else:
#        count.update({i.lower(): 1})
# count = {i: words.count(i) for i in words}
# print('\n'.join("{} {}".format(key, value) for (key, value) in count.items()))
# print(f'{key} {values}'.format(key, values) for (key, values) in count.items())

def word_counter(words):
    counts = {i: words.count(i) for i in words}
    print('\n'.join("{} {}".format(k, v) for (k, v) in counts.items()))

def main():
    words = input().lower().split()
    word_counter(words)
main()