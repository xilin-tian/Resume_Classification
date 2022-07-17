from recommend_profiles import find_resumes
import pytest
import pandas as pd

def test_find_resumes():
    skills = []
    resume = pd.DataFrame({'ID':[1,2], 'Category':['HR','HR'],'skills':[['python'],[]]})
    assert list(find_resumes(skills, resume, 10)["Similarity"]) == [0.0 , 0.0]

def test_find_resumes_simple_skills():
    skills = ['python']
    resume = pd.DataFrame({'ID':[1,2], 'Category':['HR','HR'],'skills':[['python'],[]]})
    assert list(find_resumes(skills, resume, 10)["Similarity"]) == [1.0 , 0.0]