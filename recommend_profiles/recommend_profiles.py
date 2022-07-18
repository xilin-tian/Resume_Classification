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
    myset = []
    subset = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            subset.append(ent.text.lower())
    myset.append(subset)
    subset = list(set(subset))
    subset.sort()
    return subset

def skills_to_doc(skills: list) -> str:
    lower_case_skills = (map(lambda x: x.lower(), skills))
    sort_skills = sorted(lower_case_skills)
    lst_of_string =  ' '.join(str(e) for e in sort_skills)
    return lst_of_string


def stringfied_list_to_doc(skills: str) -> str:
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
        if len(x) == 0:
            nlp_score = 0
        else:
            nlp_score = nlp(x).similarity(nlp(eg))
        similarity_score.append(nlp_score)
    append_resume['Similarity'] = similarity_score
    append_resume = append_resume.sort_values(by=['Similarity'], ascending=False)
    return append_resume.head(max_matches)