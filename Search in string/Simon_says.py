# Simon says
# Do you know the game "Simon says?" The
# instructor, "Simon", says what the players should
# do, e.g. "jump in the air" or "close your eyes". The
# players should follow the instructions only if the
# phrase starts with "Simon says". Now let's
# implement a digital version of this game! We will
# modify it a bit: the correct instructions may not only
# start but also end with the words "Simon says".
# But be careful, instructions can be only at the
# beginning, or at the end, but not in the middle!

# Write a function that takes a string with
# instructions: if it starts or ends with the words
# "Simon says", your function should return the
# string "I ", plus what you would do: the
# instructions themselves. Otherwise, return "I
# won't do it!".

# You are NOT supposed to handle input or call your
# function, just implement it.

def what_to_do(instructions):
    return "I " + instructions.replace("Simon says", "").strip(" ") if instructions.startswith("Simon says") or instructions.endswith("Simon says") else "I won't do it!"

print(what_to_do("Simon says make a wish"))