# There's a list info about people who search for a date. For
# each person, a few parameters are specifies: their gender, age, 
# hobbies, and city.

potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"}, 
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"}, 
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]

# Help a new user write a function that selects from the 
# given list people older than 30, interested in art, and living
# in Berlin. The function should return their names as a 
# string, separated by a comma and a space, e.g. "Maria,
# Daniel" for the example list above.

def select_dates(potential_dates):
    dates = {i.get("name") for i in potential_dates 
             if i.get("age") > 30 
             and "art" in i.get("hobbies") 
             and "Berlin" in i.get("city")}
    return ", ".join("{}".format(i) for i in dates)

def main():
    print(select_dates(potential_dates))
main()