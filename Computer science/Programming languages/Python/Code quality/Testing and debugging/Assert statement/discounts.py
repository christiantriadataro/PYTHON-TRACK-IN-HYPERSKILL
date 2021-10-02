# Imagine you are at the stationery. You want to buy a cheap 
# pencil, so you are looking for discounts. You have found some
# price labels. The first one is the standard price, the second
# one is a reduced price. You want to buy a pencil if the
# discount is more than 50%.

# Write a function called discounts() that takes two prices, 
# the standard one and the discounted one. If the discount is
# more than 50%, return the message: "I will buy it!". If it
# is less, use the assert keyword.

# You do not need to take any input or call the function 
# yourself.

def discounts(x, y):
    assert y < x * 0.5
    return "I will buy it!"