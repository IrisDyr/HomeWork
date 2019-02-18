
students_dict = {
    
       'first_student': {
            'name': 'Iris Dyrmishi',
            'school': 'AUBG',
            'grades': [92.0, 98.8, 90.2]
        },
        'second_student': {
            'name': 'Jake Peralta',
            'school': 'AUBG',
            'grades': [100.0, 32.8, 80.7]
        },
        'third_student': {
            'name': 'Amy Santiago',
            'school': 'AUBG',
            'grades': [80.2, 90.3, 33.4]
        }
}

for keys in students_dict:
    print("Student ",students_dict[keys]['name'], "has an average grade of ",sum(students_dict[keys]['grades'])/len(students_dict[keys]['grades']),"\n\n")
 