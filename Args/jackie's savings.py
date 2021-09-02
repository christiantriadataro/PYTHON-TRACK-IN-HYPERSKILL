# Jackie earned €1,000 and now he wants to put these savings in
# the bank for several months. However, he has not yet decided on
# the exact term for the contribution.

# Suppose that the bank that Jackie chose has offers for different
# amounts of time. The interest rates also change from month to 
# month. So, let's say he decides to put money for three months,
# and the bank sets interest reates of 5%, 7%, and 4%. The actual
# algorithm will be as follows:

# Amount after the first month: €1,000 * 1.05 = €1,050
# Amount after the second month: €1,050 * 1.07 = €1,123.5
# Amount after the third month: €1,123.5 * 1.04 = €1,168.44

# Thus, the final amount will be equal to €1,168.44. Round the 
# value to two decimal places!

# Your task is to correct the errors in the definition of the 
# final_deposit_amount() function and implement it. The 
# function should calculate and return the amount of money that
# Jackie will receive at the end. Note that we use interest rates as
# positional arguments to the function. # We also have a keyword-
# only argument amount. You do not need to call a function, just
# implement it.

def final_deposit_amount(*interest, amount=1000):
    for n in interest:
        amount *= n / 100 + 1
    return round(amount,2)


print(final_deposit_amount(5, 7, 4))
