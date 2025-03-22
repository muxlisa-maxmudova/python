grades = {
    'Munisa': 2,
    'Muslima': 3,
    'Mukhlisa': 2,
    'Mary': 5,
    'Samantha': 10,
    'Catherina':10,
    'Isaac': 8,
}

def render_grades():
    for name in grades.keys():
        print(f'{name} got {grades[name]}') # we do not need '' when we declare by ourselves
render_grades()