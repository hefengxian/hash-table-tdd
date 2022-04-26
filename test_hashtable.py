from hashtable import HashTable

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
    assert HashTable(capacity=3).values == [None, None, None]
