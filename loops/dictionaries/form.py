def main():
    person = {'name': 'Munisa', 'age': 5, 'grade': 5}
    person['sex'] = 'Female'
    person.update({'status': 'good', 'behaviour': 'acceptable'})
    print(create_form(person))
def create_form(person):
    return f'''
    ======= FORM =======
    
    Name: {person.get('name', 'Unknown')}
    Age: {person.get('age', 'Unknown')}
    Sex: {person.get('sex', 'Undefined')}
    Grade: {person.get('grade', 0)}
    Status in e-card: {person.get('status', 'None')}
    Behaviour: {person.get('behaviour', 'Unknown')}

    ====================
   '''
main()