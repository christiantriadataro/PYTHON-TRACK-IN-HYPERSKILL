# Ronald is filling up his dataset with new data to classify species
# of iris flowers better. Define a function add_iris() to help him
# a bit.

# The parameters for eac new sample include 4 obligatory
# parameters:
# - id_n
# - species
# - petal_length
# - petal_width

# There may also be some additional features. Collect keyword
# arguments to getm them.

# Your function should add key-value pairs into an existing
# dictionary called iris. Predictably, id_n will serve as a key, 
# and its value should be a dictionary with the rest of the 
# specified parameters.

# Please, don't print or return anything: you only need to update
# the dictionary iris.

# For example, after calling the function for the first time
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale
# lilac) the dictionary iris will look like this {0: {'species':
# 'Iris versicolor', 'petal_length': 4.0, 'petal_width': 1.3, 
# 'petal_hue': 'pale lilac'}}. Pay attention to the last pair that
# represents a new feature.

iris = {}
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')

def add_iris(*data, **features):
    iris[data[0]] = {'species': data[1],
                      'petal_length': data[2],
                      'petal_width': data[3], **features}

add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
print(iris)

iris = {}


def add_iris(id_n, species, petal_length, petal_width, **features):
    global iris
    new_iris = {}
    new_iris.update(id_n={'species': species, 'petal_length': petal_length,
                       'petal_width': petal_width})
    iris = {**new_iris, **features}