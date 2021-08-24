# You have a predefined string vowels that contains all letter
# designating vowel sounds. Write a program that coounts the
# number of vowels in the variable string and prints this number.
count = 0
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
for c in string:
    if c in vowels:
        count += 1
print(count)