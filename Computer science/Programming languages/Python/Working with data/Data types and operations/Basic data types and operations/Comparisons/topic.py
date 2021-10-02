# Theory: Comparisons

# Writing code without comparing any values in it will get you
# only so far. Now, it's time to master this skill.

# 1. Comparison operators
# Comparison or relation operations let you compare two values
# and determine the relation between them. There are ten
# comparison operators in Python:

# < strictly less than
# <= less than or equal
# > strictly greater than
# >= greater than or equal
# == equal
# != not equal
# is object identity
# is not negated object identity
# in membership
# not in negated membership.

# The result of applying these operators is always bool. The
# following sections focus on the first six operators (<, <=, >,
# >=, ==, !=), but you can find more details about identity and
# membership testing in the next topics.

# 2. Comparing integers
# In this topic, we will cover only integer comparison.

a = 5
b = -10
c = 15

result_1 = a < b   # False
result_2 = a == a  # True
result_3 = a != b  # True
result_4 = b >= c  # False
# Any expression that returns an integer is a valid comparison
# operand too:

calculated_result = a == b + c  # True
# Given the defined variables a, b and c, we basically check if
# 5 is equal to -10 + 15, which is true.

# Comparison chaining
# Since comparison operations return boolean values, you can
# join them using logical operators. In this case, it is important
# to know their priority, i.e. which one is executed first. All
# comparison operations have the same priority, and it is lower
# than that of any arithmetic, shifting, or bitwise operation.

x = -5
y = 10
z = 12

result = x < y and y <= z  # True
# In Python, there is a fancier way to write complex comparisons.
# It is called chaining. For example, x < y <= z is almost
# equivalent to the expression you saw in the last example. The
# difference is that y is evaluated only once.

result = 10 < (100 * 100) <= 10000  # True, the multiplication is evaluated once

#       Please pay attention to the fact that tools for code quality
#       often recommend chaining comparisons instead of joining them.

# Comparison chaining, however, should be used carefully
# because sometimes expressions might get tricky, so the result
# would depend on the operators' order and how the parentheses
# are put. Consider this example:

a = 1
b = 2
c = 3
e = 4
f = 5
g = 6

print(b + c <= e or f + g >= e == f == 5)      # False
print((b + c <= e or f + g >= e) == (f == 5))  # True

# The first expression is False because it is evaluated
# consequently: the part b + c <= e or f + g >= e is True but
# it is not equal to f, so the whole expression is already False.
# In the second case, both operands are Trueand True equals
# True, so the final expression is also True.

# 4. Logic & arithmetics
# Let's look at another interesting case. At the beginning of the
# topic, we learned that the result of applying comparison
# operators is always bool. However, if there is a logical and
# arithmetic part in an expression, we might see unusual
# behavior:

# True and-expressions return the result of the last operation:
print(b + c * f >= e and (f + g) * c)  # 33
print((f + g) * c and b + c * f >= e)  # True

# False and-expressions return a boolean False value:
print(b + c * f <= e and (f + g) * c)  # False
print((f + g) * c and b + c * f <= e)  # False

# True or-expressions return the result of the first operation:
print(b + c * f >= e or (f + g) * c)  # True
print((f + g) * c or b + c * f >= e)  # 33

# True-False or-expressions return the True part:
print((f + g) * c or b + c * f <= e)  # 33
print(b + c * f <= e or (f + g) * c)  # 33

# It might look confusing at first sight but, if you think about it,
# every printed value is perfectly legal and complies with
# common mathematical logic.

# 5. Summary
# In this topic, we familiarized ourselves with Python comparison
# operators, learned how to compare integers, and use
# comparison chaining. These basic operators will definitely be a
# great help to you in the future!
