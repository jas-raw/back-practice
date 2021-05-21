from typing import Optional
from enum import Enum
from pydantic import BaseModel

class Genero(str, Enum):

    male = "male"
    female = "female"

class Student(BaseModel):

	id: str
	complete_name: str
	document: str
	age: int
	gender: Genero
	note: Optional[int]
	autoevaluacion: Optional[int]
