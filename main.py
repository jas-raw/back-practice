from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from models import Student
from bd import read_all, write_one, update_one

app = FastAPI()

#Metodos de admin
@app.post("/api/v1/students")
async def create_student(student_in: Student, auth: str = Header(None)):
	if auth == 'admin':
		students = read_all()['students']
		for student in students:
			if student['document'] == student_in.document:
				return JSONResponse(status_code=409, content={"message": "El documento ya se encuentra registrado"})
		results = write_one(students, student_in.dict())
		return {'results': results, "message": None}
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.get("/api/v1/students")
async def listar_studiantes(auth: str = Header(None)):
	if auth == 'admin':
		results = read_all()['students']
		return {'results': results, "message": None}
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.patch("/api/v1/students/nota/{document}")
async def agregar_nota(document: str, nota: int, auth: str = Header(None)):
	if auth == 'admin':
		if nota >= 0 and nota <= 5 and isinstance(nota, int):
			students = read_all()['students']
			for student in students:
				if student['document']==document:
					student['note']=nota
					results = update_one(students, student)
					return {'results': results, "message": None}
			return {"message": "No se encontro el documento"}
		return {"message": "La nota debe estar entre 0 y 5 y ser entero"}
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.get("/api/v1/students/promedio")
async def promedios(auth: str = Header(None)):
	if auth == 'admin':
		students = read_all()['students']
		suma=sum([student['note'] for student in students])
		cont = len(students)
		res = str(suma/cont).split('.')
		if len(res) == 1:
			results = float(res[0])
		else:
			apr=0
			if len(res[1]) >= 3:
				if int(res[1][2]) >= 5:
					apr = 0.01
			results = float(res[0]+'.'+res[1][0:2])+apr
		return {'results': results, "message": None}
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

#Metodos de students
@app.get("/api/v1/students/one")
async def leer_por_id(document: str, auth: str = Header(None)):
	if auth == 'student':
		students = read_all()['students']
		for student in students:
			if student['document']==document:
				return {'results': student, "message": None}
		return {"message": "No se encontro el documento"}
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.patch("/api/v1/students/auto/{document}")
async def set_autoevaluacion(document: str, autoevaluation: int, auth: str = Header(None)):
	if auth == 'student':
		if autoevaluation >= 0 and autoevaluation <= 5 and isinstance(autoevaluation, int):
			students = read_all()['students']
			for student in students:
				if student['document']==document:
					student['autoevaluation']=autoevaluation
					results = update_one(students, student)
					return JSONResponse(status_code=200, content={'results': results, "message": None})
			return JSONResponse(status_code=404, content={"message": "No se encontro el documento"})
		return JSONResponse(status_code=409, content={"message": "La autoevaluacion debe estar entre 0 y 5 y ser entero"})
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})
