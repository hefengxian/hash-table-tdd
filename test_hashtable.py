import pytest
from hashtable import HashTable, BLANK

"""
Test case should be as independent and atomic as possible

given-when-then convention
    # Given
    # When
    # Then
"""

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=10)) == 10

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK]

def test_should_insert_key_value_pairs():
    hashtable = HashTable(capacity=100)

    hashtable['hola'] = "Hello"
    hashtable[98.2] = 39
    hashtable[False] = True

    assert 'Hello' in hashtable.values
    assert 39 in hashtable.values
    assert True in hashtable.values
    assert len(hashtable) == 100

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=10).values

def test_should_insert_none_value():
    hashtable = HashTable(capacity=10)
    hashtable['k'] = None
    assert None in hashtable.values

@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass