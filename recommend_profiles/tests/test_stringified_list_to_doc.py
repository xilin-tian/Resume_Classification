from recommend_profiles import stringified_list_to_doc
import pytest

def test_stringified_list_to_doc_empty():
    assert stringified_list_to_doc("[]") == ''

def test_stringified_list_to_doc_empty_string():
    assert stringified_list_to_doc("") == ''

def test_stringified_list_to_doc():
    assert stringified_list_to_doc("['a', 'b']") == 'a b'


def test_stringified_list_to_doc_one_string_in_bracket():
    assert stringified_list_to_doc("[a]") == 'a'

def test_stringified_list_to_doc_one_string_without_bracket():
    assert stringified_list_to_doc("a") == 'a'
