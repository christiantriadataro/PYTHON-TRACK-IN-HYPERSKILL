# Imagine you have a list of students and their grades for an exam:

students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
print([student[0] for student in students if student[1] == 'A'])