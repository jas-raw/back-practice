import json

def read_js():
    db = open('students_list.json', 'r')
    data = json.load(db)
    return data
