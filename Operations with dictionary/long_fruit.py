# dictionary = {key: value for element in iterable}
fruits = ['apple', 'kiwi', 'banana', 'orange', 'apricot']
fruit_dict = {element: len(element) for element in
              fruits if len(element) > 5}
print('\n'.join("{} {}".format(element, leng) for (element, leng) in fruit_dict.items()))             