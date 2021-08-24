# Let's say you were asked to create a program for a restaurant: a
# visitor enters what kind of food they would like to order and
# gets back the restaurant's offer.

# The restaurant has just opened so its menu contains only a few
# options:

# - pizza: Margherita, Four Seasons, Neapolitan, Vegetarian,
#   Spicy
# - salad: Caesar salad, Green salad, Tuna salad, Fruit salad
# - soup: Chicken soup, Ramen, Tomato soup, Mushroom
#   cream soup

# If the visitors ask for something that is not on the menu, the
# program should write "Sorry, we don't have it in the menu."
user = input()
menu = {'pizza': ['Margherita', 'Four Seasons', 'Neapolitan', 'Vegetarian', 'Spicy'],
        'salad': ['Caesar salad', 'Green salad', 'Tuna salad', 'Fruit salad'],
        'soup': ['Chicken soup', 'Ramen', 'Tomato soup', 'Mushroom cream soup']}

print(f'{menu[user]}'.strip("[]").replace("'", "") if user in menu.keys() else "Sorry, we don't have it in the menu")