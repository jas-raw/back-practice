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
		return JSONResponse(status_code=200, content={'results': results, "message": None})
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.get("/api/v1/students")
async def listar_usuarios(auth: str = Header(None)):
	if auth == 'admin':
		results = read_all()['students']
		return JSONResponse(status_code=200, content={'results': results, "message": None})
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.patch("/api/v1/students/{student_id}")
async def agregar_nota(student_id: str, nota: int, auth: str = Header(None)):
	if auth == 'admin':
		if nota >= 0 and nota <= 5 and isinstance(nota, int):
			students = read_all()['students']
			for student in students:
				if student['document']==student_id:
					student['note']=nota
					results = update_one(students, student)
					return JSONResponse(status_code=200, content={'results': results, "message": None})
			return JSONResponse(status_code=404, content={"message": "No se encontro el documento"})
		return JSONResponse(status_code=409, content={"message": "La nota debe estar entre 0 y 5 y ser entero"})
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

#Metodos de students
@app.get("/api/v1/students/{student_id}")
async def leer_por_id(auth: str = Header(None)):
	if auth == 'student':
		results = read_all()['students']
		return JSONResponse(status_code=200, content=results['students'])
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.patch("/api/v1/students/")
async def set_autoevaluacion(auth: str = Header(None)):
	if auth == 'student':
		results = read_all()['students']
		return JSONResponse(status_code=200, content=results['students'])
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})
