# Yearly income

# The file salary.txt contains a monthly salary of all employess in
# the company. Assume that the monthly salary is fixed and each
# employee is mentioned once. So, each number (an integer)
# written on a separate line corresponds to a particular employee:

# 3500
# 4780
# 6666
# ....

# According to the example, the first worker gets 3,500 per
# month, the second one 4,780 and the third 6,666 etc.

# calculate how much each employee earns per year and save
# their yearly income to a file salary_year.txt. Similarly to the
# original file, each income should be on a separate line. Preserve
# the order as it helps identify an employee.

# Files are read and written as strings, so don't forget to do
# necessary conversions!

with open('salary.txt', 'r') as file, open('salary_year.txt', 'w') as new_file:
    file.write('\n'.join(str(int(x) * 12) for x in new_file))

