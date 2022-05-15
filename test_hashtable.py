import pytest
from pytest_unordered import unordered
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

def test_should_report_length_of_empty_hash_table():
    assert len(HashTable(capacity=10)) == 0

def test_should_create_empty_pair_slots():
    assert HashTable(capacity=3)._slots == [None, None, None]

def test_should_insert_key_value_pairs():
    hashtable = HashTable(capacity=100)

    hashtable['hola'] = "Hello"
    hashtable[98.2] = 39
    hashtable[False] = True

    assert ('hola', 'Hello') in hashtable.pairs
    assert (98.2, 39) in hashtable.pairs
    assert (False, True) in hashtable.pairs
    assert len(hashtable) == 3

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=10).values

def test_should_insert_none_value():
    hashtable = HashTable(capacity=10)
    hashtable['k'] = None
    assert ('k', None) in hashtable.pairs

# @pytest.mark.skip
# def test_should_not_shrink_when_removing_elements():
#     pass

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

def test_should_delete_key_value_pair(hash_table):
    assert 'hola' in hash_table
    assert ('hola', 'Hello') in hash_table.pairs
    assert len(hash_table) == 3

    del hash_table['hola']
    assert 'hola' not in hash_table
    assert ('hola', 'Hello') not in hash_table.pairs
    assert len(hash_table) == 2

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
    assert len(hash_table) == 3

def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs

def test_should_return_duplicate_values():
    ht = HashTable(capacity=10)
    ht['Alice'] = 23
    ht['Bob'] = 34
    ht['Joe'] = 34
    assert [23, 34, 34] == sorted(ht.values)

def test_should_get_values(hash_table):
    assert unordered(hash_table.values) == ['Hello', True, 39]

def test_should_get_value_of_empty_hash_table():
    assert HashTable(capacity=100).values == []

def test_should_return_copy_of_values(hash_table):
    assert hash_table.values is not hash_table.values

def test_should_get_keys(hash_table):
    assert hash_table.keys == {'hola', 98.2, False}

def test_should_get_key_of_empty_hash_table():
    # there is no empty set literal 
    assert HashTable(capacity=10).keys == set()

def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys

def test_should_return_pairs(hash_table):
    assert hash_table.pairs == {
        ("hola", "Hello"),
        (98.2, 39),
        (False, True)
    }

def test_should_get_pairs_of_empty_hash_table():
    assert HashTable(capacity=10).pairs == set()

def test_should_convert_to_dict(hash_table):
    dictionary = dict(hash_table.pairs)
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == unordered(hash_table.values)

def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=0)

def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=-10)

def test_should_report_length(hash_table):
    assert len(hash_table) == 3

def test_should_report_capacity_of_empty_hashtable():
    assert HashTable(capacity=10).capacity == 10

def test_should_report_capacity(hash_table):
    assert hash_table.capacity == 100

def test_should_iterate_over_keys(hash_table):
    for k in hash_table:
        assert k in ('hola', 98.2, False)

def test_should_iterate_over_values(hash_table):
    for value in hash_table.values:
        assert value in ('Hello', 39, True)

def test_should_iterate_over_pairs(hash_table):
    for key, value in hash_table.pairs:
        assert key in hash_table.keys
        assert value in hash_table.values

def test_should_use_dict_literal_for_str(hash_table):
    assert str(hash_table) in {
        "{'hola': 'Hello', 98.2: 39, False: True}",
        "{'hola': 'Hello', False: True, 98.2: 39}",
        "{98.2: 39, 'hola': 'Hello', False: True}",
        "{98.2: 39, False: True, 'hola': 'Hello'}",
        "{False: True, 'hola': 'Hello', 98.2: 39}",
        "{False: True, 98.2: 39, 'hola': 'Hello'}",
    }

def test_should_create_hashtable_from_dict():
    dictionary = {'hola': 'Hello', 98.2: 39, False: True}
    hash_table = HashTable.from_dict(dictionary)
    assert hash_table.capacity == len(dictionary) * 10
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.pairs == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())

def test_should_have_canonical_string_representation(hash_table):
    assert repr(hash_table) in {
        "HashTable.from_dict({'hola': 'Hello', 98.2: 39, False: True})",
        "HashTable.from_dict({'hola': 'Hello', False: True, 98.2: 39})",
        "HashTable.from_dict({98.2: 39, 'hola': 'Hello', False: True})",
        "HashTable.from_dict({98.2: 39, False: True, 'hola': 'Hello'})",
        "HashTable.from_dict({False: True, 'hola': 'Hello', 98.2: 39})",
        "HashTable.from_dict({False: True, 98.2: 39, 'hola': 'Hello'})",
    }

def test_should_compare_equal_to_itself(hash_table):
    assert hash_table == hash_table

def test_should_compare_equal_to_copy(hash_table):
    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()

def test_should_compare_equal_different_key_value_order():
    h1 = HashTable.from_dict({'a': 1, 'b': 2, 'c': 3})
    h2 = HashTable.from_dict({'b': 2, 'a': 1, 'c': 3})
    print(h1)
    print(h2)
    assert h1 == h2

def test_should_compare_unequal(hash_table):
    other = HashTable.from_dict({'aaa': 'bbb'})
    assert hash_table != other

def test_should_compare_unequal_another_data_type(hash_table):
    assert hash_table != 23

def test_should_copy_keys_values_pairs_capacity(hash_table):
    copy = hash_table.copy()
    assert copy is not hash_table
    assert set(copy.keys) == set(hash_table.keys)
    assert unordered(copy.values) == hash_table.values
    assert set(copy.pairs) == set(hash_table.pairs)
    assert copy.capacity == hash_table.capacity

def test_should_compare_equal_different_capacity():
    data = {'a': 1, 'b': 2}
    h1 = HashTable.from_dict(data, 30)
    h2 = HashTable.from_dict(data, 50)
    assert h1 == h2
