# Re-write the following piece of code using the lambda keyword:
# def func(x):
#     if x % 10 == 0:
#         return "x ends with 0"
#     else:
#         return x" doesn't end with 0"

# You are not supposed to handle input or invoke this function. Just
# re-write it!

func = lambda x: "x ends with 0" if x % 10 == 0 else "x doesn't end with 0"

print(func(20))