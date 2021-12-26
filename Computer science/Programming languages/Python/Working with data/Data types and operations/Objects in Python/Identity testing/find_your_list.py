# You play a game with your friends. You give them a non-empty list
# of integers and they create a list of lists, which contains your list
# and some other non-empty list in some order.  Your task is to find
# your list among other lists.

# You should write a function find_my_list(all_list, my_list).
# where the first argument is the list of lists and the second
# argument is the list of integers that you should find. The function
# should return the position of my_list in all_lists. The list in
# all_lists are numbered from zero. It's guaranteed that an
# element exists in all_lists.

def find_my_list(all_lists, my_list):
    for i, lst in enumerate(all_lists):
        # Change the next line
        if lst is my_list:
            return i
    return None