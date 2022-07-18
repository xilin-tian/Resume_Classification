from recommend_profiles import skills_to_doc
import pytest

def test_skills_to_doc_empty():
    assert skills_to_doc([]) == ""

def test_skills_to_doc_one():
    assert skills_to_doc(["Python"]) == "python"

def test_skills_to_doc_multi():
    assert skills_to_doc(["A","b","C","d"]) == "a b c d"

def test_skills_to_doc_order():
    assert skills_to_doc(["A","c","B","d"]) == "a b c d"