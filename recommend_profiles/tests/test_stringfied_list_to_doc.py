from recommend_profiles import stringfied_list_to_doc
import pytest

def test_stringfied_list_to_doc_empty():
    assert stringfied_list_to_doc("[]") == ''

def test_stringfied_list_to_doc_empty_string():
    assert stringfied_list_to_doc("") == ''

def test_stringfied_list_to_doc():
    assert stringfied_list_to_doc("['a', 'b']") == 'a b'


def test_stringfied_list_to_doc_one_string_in_bracket():
    assert stringfied_list_to_doc("[a]") == 'a'

def test_stringfied_list_to_doc_one_string_without_bracket():
    assert stringfied_list_to_doc("a") == 'a'
