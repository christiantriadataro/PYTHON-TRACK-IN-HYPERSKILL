# In online test games, there is usually a limited number of lives:
# if, for example, you make 3 mistakes, you lose and do not
# continue with the game. Imagine you are trying to implement
# that system to an online test game.

# The input format:
# A line with N user answers in a game separated by a space: C
# for a correct answer and I for an incorrect answer.

# The user always had 3 lives. The user loses when they make
# their third mistake. If the user makes no more than 2 mistakes,
# they win.

# The output format:
# If the user loses the game, print "Game over" and their score
# (the number of correct answers). If the user wins, print "You
# won" and their score. The message should be printed without
# quotation marks. The message and the score shoule be printed
# on separate lines.

scores = input().split()
# put your python code here
count = 0
lose = 0
for score in scores:
    if lose > 2:
        break
    if score == 'C':
        count += 1
    else:
        lose += 1
print("You won" if lose < 3 else "Game over")
print(count)