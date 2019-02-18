
from module import module_dict

student_dict = {
    'name': 'Iris Dyrmishi',
    'school': 'AUBG',
    'grades': [80.5, 96.2, 82.3]
}

print(student_dict,"\n\n")

grade_string = input("Enter all the grades separated by a comma (,):\n\n")

grade_float = list(map(float, grade_string.split(",")))

for grades in grade_float:
    module_dict.add_grade(student_dict,grades)

print(student_dict)