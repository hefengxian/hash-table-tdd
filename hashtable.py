from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError('Capacity must be a positive number')
        self._slots = capacity * [None]
    
    def __len__(self):
        return len(self.pairs)

    def __setitem__(self, key, value):
        self._slots[self._index(key)] = Pair(key, value)
    
    def __getitem__(self, key):
        pair = self._slots[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        if key in self:
            self._slots[self._index(key)] = None
        else:
            raise KeyError(key)

    def _index(self, key):
        return hash(key) % self.capacity

    @property
    def pairs(self):
        return {pair for pair in self._slots if pair}

    @property
    def values(self):
        return [pair.value for pair in self.pairs]

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}

    @property
    def capacity(self):
        return len(self._slots)

    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            # !r enforce to call repr() 
            pairs.append(f"{key!r}: {value!r}")
        return "{%s}" % (', '.join(pairs))
    
    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
    
    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}.from_dict({str(self)})"

    def __eq__(self, other):
        if other is self:
            return True
        if type(other) is not type(self):
            return False
        return set(other.pairs) == set(self.pairs)

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)