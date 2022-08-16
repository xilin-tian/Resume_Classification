from fastapi import FastAPI
import pandas as pd
from typing import List
from recommend_profiles import parse_skills
from model import Resume, Specialization, TimeZone

app = FastAPI()


@app.get("/parse_skills/{resume}")
# Extract the skills as an output of list of strings from the input(string)
def extract_skills(resume: str):
    return parse_skills(resume)



from recommend_profiles import find_resumes

sample_resume = pd.DataFrame({'profile_id':[1,2], 'name':['Tom','Jerry'],'skills':[['python'],[]]})

# Original Database with profile_id: int, 
#                        name: str, 
#                        skills: list of strings, 
#                        specialization: Digital marketing/Machine learning/UX Design
#                        location: str,
#                        timezone: HST or HDT/AKST or AKDT/PST or PDT/MST or MDT/CST or CDT/EST or EDT/NST or NDT/AST or ADT
#                        position: str,
#                        about: str, imported class[Resume] from model.py 
db : List[Resume]  = [
    Resume(
        profile_id = 1, 
        name = "Tom", 
        skills = ["python"], 
        specialization= Specialization.Machine_learning,
        location= "LA",
        timezone = TimeZone.PST_PDT,
        position = "Data analyst",
        about = 'Tom knows Python'
        ),
    Resume(
        profile_id = 2, 
        name = "Jerry", 
        skills = ["python"], 
        specialization= Specialization.Machine_learning,
        timezone = TimeZone.PST_PDT,
        about = 'Jerry knows nothing'
        )
]

@app.get("/users/")
# showing the database
def fetch_users():
    return db


@app.post("/users/")
# Add new users to the origional database.
def register_user(user: Resume):
    db.append(user)
    return db


@app.get("/find_resumes/{skills}/{max_matches}")
def find_match_resumes(skills: str, max_matches: int):
    from recommend_profiles import stringified_list_to_doc
    lst = [stringified_list_to_doc(skills)]
    answer = find_resumes(lst, sample_resume, max_matches)
    return answer.to_json(orient="index")