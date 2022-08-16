import jsonlines
import pandas as pd
import numpy as np
import re
import spacy
import warnings 
warnings.filterwarnings('ignore')

nlp = spacy.load('en_core_web_md')


from spacy.pipeline import EntityRuler
ruler = nlp.add_pipe("entity_ruler", name="ruler", before="ner")
ruler.from_disk("jz_skill_patterns.jsonl")

def parse_skills(resume: str) -> list:
    doc = nlp(resume)
    skills = [entity.text.lower() for entity in doc.ents if entity.label_ == "SKILL"]
    skills = list(set(skills))
    skills.sort()
    return skills

def skills_to_doc(skills: list) -> str:
    lower_case_skills = (map(lambda x: x.lower(), skills))
    sort_skills = sorted(lower_case_skills)
    lst_of_string =  ' '.join(str(e) for e in sort_skills)
    return lst_of_string


def stringified_list_to_doc(skills: str) -> str:
    a = re.sub(r'\'', '', skills)
    b = re.sub(r'\[|\]', '',a)
    c = re.split(r"[,]\s*", b)
    return skills_to_doc(c)

def find_resumes(skills: list, resume: pd.DataFrame, max_matches: int) -> pd.DataFrame:
    similarity_score= []
    append_resume = resume
    eg = skills_to_doc(skills)
    for i in range(resume.shape[0]):
        x = skills_to_doc(resume['skills'].loc[i])
        if len(x) == 0 or len(eg) == 0:
            nlp_score = 0
        else:
            nlp_score = nlp(x).similarity(nlp(eg))
        similarity_score.append(nlp_score)
    append_resume['Similarity'] = similarity_score
    append_resume = append_resume.sort_values(by=['Similarity'], ascending=False)
    return append_resume.head(max_matches)

def university_parser(doc: str) -> list:
    tokenized_doc = nlp(doc)
    ORG_list = [ent.text for ent in tokenized_doc.ents if ent.label_ == "ORG"]
    lst = ["university","University","UNIVERSITY","institude","Institude","INSTITUDE","college","College","COLLEGE"]
    university = []
    for org in ORG_list:
        for word in lst:
            if word in org:
                university.append(org)
    return university