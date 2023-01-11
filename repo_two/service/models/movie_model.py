from typing import List
from pydantic import BaseModel

'''
Pydantic is a Python library for data modeling/parsing that has efficient error handling 
and a custom validation mechanism. As of today, Pydantic is used mostly in the FastAPI framework 
for parsing requests and responses
because Pydantic has built-in support for JSON encoding and decoding
'''


class MovieModel(BaseModel):
    title: str
    keywords: List[str] = []
    director: str
    year: int
