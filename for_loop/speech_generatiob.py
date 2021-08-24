# Here is your chance to write instructions for a text-to-speech
# system. Let's focus on reading phone numbers aloud. The input
# phone number will consist solely of digits. Print the name of 
# each digit on a new line for the system to read them one by one.
numbers = {'1':'one', '2':'two', '3':'three', '4':'four', 
           '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
user = list(input())
for n in user:
    if n in numbers.keys():
        print(numbers.get(n))