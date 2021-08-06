# The output should be user-friendly, but the code part is also
# important. Well-structured and readable code is very important
# for being a good programmer. Now it's up to you to decide,
# which formatting method to choose.

# Imagine you need to compose a dynamic URL for every certain
# user with user-specific details. Suppose, you want to send
# different URLs for every user, depending on their name and
# profession. The base would be something like

# "http://example.com/*nickname*/desirable/*profession*/profil
# e", where nickname and profession are prompts from a user and 
# are dynamic.

# Read the nickname and profession of the user from the input
# and print a user-specific URL. Don't bother about any rules of
# composing the URLs and just use raw input to accomplish the
# task.

# Sample Input 1:
# raybeam
# cereal-killer

# Sample Output 1:
# http://example.com/raybeam/desirable/cereal-killer/profile

# Sample Input 2:
# AnnMelon
# bodybuilder

# Sample Output 2:
# http://example.com/AnnMelon/desirable/bodybuilder/profile

# using str.format method
# print("http://example.com/{nickname}/desirable/{profession}/profile".format(nickname = input(), profession = input()))

# using formatted string literals without variable
print(f"http://example.com/{input()}/desirable/{input()}/profile")

# using formated string literals with variable multi-line coding
nickname = input()
profession = input()

print(f"http://example.com/{nickname}/desirable/{profession}/profile")