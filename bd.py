import json

'''Inicializacion'''

data_base = 'students_list.json'

def guardar(js: dict):
    with open('{}'.format(data_base), 'w', newline='\n') as file:
        json.dump(js, file, indent=4, ensure_ascii=False)
    return 1


'''Metodos de la base de datos'''

def read_all():
    db = open(data_base)
    data = json.load(db)
    return data

def write_one(data: list, student: dict):
    data.append(student)
    js = {
        "students": data
    }
    return guardar(js)

def update_one(students: list, student_in: dict):
    for i in range(len(students)):
        if students[i]['document'] == student_in['document']:
            students.pop(i)
            students.append(student_in)
            js = {
                "students": students
            }
            return guardar(js)
