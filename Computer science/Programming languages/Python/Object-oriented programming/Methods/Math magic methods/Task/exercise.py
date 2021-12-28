# Below you can see the class Task. Any task has a
# description and a person for finishing this
# task. In our class, these aspects are represented by
# instance attributes description and team.

# Sometimes we may want to combine tasks together
# (that is, add them up). Define the method __add__ that:

# - combines the description of two tasks. Two
#   descriptions should be on different lines;
# - combines the two teams responsible for different
#   tasks. They should be separated by a comma and a
#   whitespace.

# Here's an example:
class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, other):
        return Task(f"{self.description}\n{other.description}", f"{self.team}, {other.team}")


task1 = Task("Finish the assignment.", "Kate")
task2 = Task("Prepare the project for class.", "James, Ann")

task3 = task1 + task2
print(task3.description)       # "Finish the assignment. \nPrepare the project for class."
print(task3.team)              # "Kate, James, Ann"

