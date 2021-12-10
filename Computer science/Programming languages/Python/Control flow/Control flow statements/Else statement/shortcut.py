# The program below asks the use if they have slept enough, and
# suggests drinking either coffee or cocoa depending on the
# answer.

print("Have you had enough hours of sleep today?")
answer = input()
if answer == "yes":
    print("Let's drink cocoa!")
else:
    print("I'd recommend a coffee!")

print("Let's drink cocoa!" if answer == "yes" else "I'd recommend a coffee!")