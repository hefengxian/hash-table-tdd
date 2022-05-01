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

@pytest.fixture
def hash_table():
    hashtable = HashTable(capacity=100)
    hashtable['hola'] = "Hello"
    hashtable[98.2] = 39
    hashtable[False] = True
    return hashtable

def test_should_find_value_by_key(hash_table):
    assert hash_table['hola'] == 'Hello'
    assert hash_table[98.2] == 39
    assert hash_table[False] == True

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table['missing_key']
    assert exception_info.value.args[0] == 'missing_key'

def test_should_find_key(hash_table):
    assert 'hola' in hash_table

def test_should_not_find_key(hash_table):
    assert 'missing_key' not in hash_table
    
def test_should_get_value(hash_table):
    assert hash_table.get('hola') == 'Hello'

def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get('missing_key') is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get('missing_key', 'default') == 'default'

def test_should_get_value_with_default(hash_table):
    assert hash_table.get('hola', 'default') == 'Hello'

def test_should_delete_key_value_paire(hash_table):
    assert 'hola' in hash_table
    assert 'Hello' in hash_table.values
    assert len(hash_table) == 100

    del hash_table['hola']

    assert 'hola' not in hash_table
    assert 'Hello' not in hash_table.values
    assert len(hash_table) == 100

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table['missing_key']
    assert exception_info.value.args[0] == 'missing_key'

def test_should_update_value(hash_table):
    assert hash_table['hola'] == 'Hello'
    hash_table['hola'] = 'Bello'
    assert hash_table['hola'] == 'Bello'
    assert hash_table[98.2] == 39
    assert hash_table[False] is True
    assert len(hash_table) == 100


