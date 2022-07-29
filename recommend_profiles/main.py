from fastapi import FastAPI
import pandas as pd
from recommend_profiles import parse_skills

app = FastAPI()

@app.get("/parse_skills/{resume}")
def extract_skills(resume: str):
    return parse_skills(resume)

@app.get("/parse_skills2/")
def extract_skills(resume: list):
    return parse_skills(resume)

from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    Name: str
    skills: str
    description: Union[str, None] = None
    #tax: Union[float, None] = None

@app.post("/items/")
def create_item(item: Item):
    return item

from recommend_profiles import skills_to_doc

from recommend_profiles import find_resumes

sample_resume = pd.DataFrame({'ID':[1,2], 'Category':['HR','HR'],'skills':[['python'],[]]})

@app.get("/find_resumes/{skills}/{max_matches}")
def find_match_resumes(skills: str, max_matches: int):
    from recommend_profiles import stringified_list_to_doc
    lst = [stringified_list_to_doc(skills)]
    answer = find_resumes(lst, sample_resume, max_matches)
    return answer.to_json(orient="index")