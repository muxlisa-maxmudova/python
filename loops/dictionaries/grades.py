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
    for name, grade in grades.items():
        print(f'{name} acquired {convert(grade)}% of the programme')
def convert(points):
    return points/10*100

render_grades()
