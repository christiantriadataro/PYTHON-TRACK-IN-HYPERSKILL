# In a standard deck of cards, there are 13 of each suit. There are
# numbered cards (from 2 to 10) and face cards (Jack, Queen,
# King and Ace). If we wereto rank the face cards, Jack would be
# 11, Queen 12, King 13, and the Ace - 14.

# Write a program that calculates the average rank of one hand of
# cards. Don't forget to consider the rank of the face cards.

# The input format:
# Six values of cards, each on a separate line.

# The output format:
# The average rank of the hand.

face_cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
average = 0
for _ in range(1, 7):
    i = input()
    if i in face_cards:
        average += face_cards.get(i)
    else:
        average += int(i)
print(average / 6)