# dictionary = {key: value for element in iterable}
# plantes_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in
#                         planets_diameter_km.items() if value > 10_000}
test_dict = {"a": 43, "b": 1233, "c": 8}
# print(test_dict[min(test_dict, key = lambda k: test_dict[k])])
# print(min(i for i in test_dict.values()))
# print(max(i for i in test_dict.values()))
print("min:", min(test_dict, key=test_dict.get))
print("max:", max(test_dict, key=test_dict.get))