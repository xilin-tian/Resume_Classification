from recommend_profiles import university_parser
import pytest

def test_university_parser_empty_string():
    assert university_parser("")== []

def test_university_parser_one_string():
    assert university_parser("Tom is a student from Kansas University.")== ['Kansas University']