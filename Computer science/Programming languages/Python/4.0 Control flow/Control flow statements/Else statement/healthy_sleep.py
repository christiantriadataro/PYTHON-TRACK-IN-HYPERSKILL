# Ann watched a TV program about health and learned that it is
# recommended to sleep at least A hours per day, but
# oversleeping is also not healthy, and you should not sleep more
# than B hours. Now Ann sleeps H hours per day. If Ann's sleep
# schedule complies with the requirements of that TV program -
# print "Normal". If Ann sleeps less than A hours, output
# "Deficiency", and if she sleeps more than B hours, output
# "Excess".

# Input to this program are the three strings with variables in the
# following order: A, B, H. A is always less than or equal to B.

# Please note the letter's cases: the output should exactly
# correspendond to what required in the program, i.e. if the program
# must output "Excess", output such as "excess", "EXCESS", or
# "ExCess" will not be graded as correct.

# You should carefully think about all the conditions, which you
# need to use. Special attention should be paid to the strictness
# of used conditional operators: distinguish between < and <=;
# > and >=. In order to understand which ones to use, please
# carefully read the problem statement.

(a, b, h) = (int(input()), int(input()), int(input()))

if h < a:
    print("Deficiency")
elif h > b:
    print("Excess") 
else:
    print("Normal")
