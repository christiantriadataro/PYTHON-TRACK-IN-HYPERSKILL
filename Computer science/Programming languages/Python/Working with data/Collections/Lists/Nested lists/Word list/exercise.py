# Create a list of words from the text below that are shorter than or equal to the input
# value. Print the new list.

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
print([word for sentence in text for word in sentence if len(word) <= int(input())])