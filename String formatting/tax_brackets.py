# In progressive tax systems, tax rates change according to the
# income. Tax brackets are divisions that regulate those changes.

# Here's an example of tax brackets in a certain tax system:

# 0 — 15,527: 0% tax
# 15,528 — 42,707: 15% tax
# 42,708 — 132,406: 25% tax
# 132,407 and more: 28% tax

# Suppose we use a simplified version of taxation and apply one
# tax rate to the entire amount of money.

# Write a program that calculates the tax that a person's going to
# pay based on their income.

# The input format:

# The value of someone's taxable income (in dollars).

# The tax for {income} is {percent}%. That is
# {calculated_tax} dollars!

# Round your calculated_tax to the nearest integer.

# Sample Input 1:

# 14378
# Sample Output 1:

# The tax for 14378 is 0%. That is 0 dollars!
# Sample Input 2:

# 99999
# Sample Output 2:

# The tax for 99999 is 25%. That is 25000 dollars!
income = int(input())
calculated_tax = 0
percent = 0
if income in range(0, 15528):
    percent = 0
elif income in range(15528, 42708):
    percent = 15
elif income in range(42708, 132407):
    percent = 25
elif income >= 132407:
    percent = 28

if percent != 0:
    calculated_tax = income * (percent / 100)

print(f"The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!")

# another solution
income = int(input)
print(f"The tax for {income} is {0}")