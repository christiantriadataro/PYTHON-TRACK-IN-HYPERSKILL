# Anthony keeps track of what he eats: he writes down how many 
# calories are his meals. Use the list of dictionaries to calculate
# the total amount of calories per day and print it.

# The sample input will look like:
meals = [
        {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
        {"title": "Italian salad with fusilli and ham", "kcal": 320},
        {"title": "Bulgur with vegetables", "kcal": 350},
        {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
        {"title": "Oatmeal with honey and peanuts", "kcal": 440}]
# The output in this case should be 1705.
total = 0
# the list "meals" is already defined
# your code here
for i in meals:
    if i == 'kcal':
        total += meals.get(i)