# In the following code, the variable e is defined 5 times (the e
# imported from math package is a mathematical constant
# approximately equal to 2.7).

from math import e

e = 1

def func_1():
    e = 0
    def func_2():
        e = -1
        def func_3():
            e = 10
            print(e)
        func_3()
    func_2()
func_1()

# Assume that func_1() will be called five times, once using the
# code as written, and then four additional times after modifying
# the code by commenting out values of e from the innermost 
# definition outward. In other words, on the second run, the vlaue
# of e defined in func_3() will be commented out; on the third
# run, the value of e defined in func_2() will also be
# commented out; and so on. Place the value in the list in the
# order that they will appear when func_1() is called in this way.
