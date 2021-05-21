from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from models import Student
from bd import read_js

app = FastAPI()

#Metodos de admin
@app.post("/api/v1/students")
async def create_student(student: Student, auth: str = Header(None)):
	if auth == 'admin':
		read_js()
	return {"message": "por implementar"}

@app.get("/api/v1/students")
async def listar_usuarios(auth: str = Header(None)):
	if auth == 'admin':
		results = read_js()
		return results['students']
	return JSONResponse(status_code=401, content={"message": "No Autorizado"})

@app.patch("/api/v1/students/{student_id}")
async def agregar_nota(student_id: str, nota: int, auth: str = Header(None)):
	return {"message": ""}

#Metodos de students
@app.get("/api/v1/students/{student_id}")
async def leer_por_id(auth: str = Header(None)):
	return {"message": "por implementar"}

@app.post("/api/v1/students/")
async def set_autoevaluacion(auth: str = Header(None)):
	return {"message": "por implementar"}
