# You are given several sets with names of students in different classes. Output the set
# containing names of all the students.

# NB! You don't need to read the input; the variables containing the input data are
# already created for you.

# Sample Input 1:
# Potter Weasley
# Lovegood Corner
# Malfoy Goyle
# Bones Macmillan

gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())
print(gryffindor | ravenclaw | slytherin | hufflepuff)