class HashTable:
    """A simple Hash Table implementation from scratch. Uses Linear Probing"""

    def __init__(self, capacity=10):
        self.capacity = capacity
        self._BLANK = object()
        self._DELETED = object()
        self.order = []
        self.slots = [self._BLANK] * capacity
        self._load_factor_threshold = 0.6

    def _get_index(self, key):
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        if len(self) / self.capacity >= self._load_factor_threshold:
            self._resize()

        index = self._get_index(key)
        for _ in range(self.capacity):
            slot = self.slots[index]

            if slot is self._BLANK or slot is self._DELETED:
                self.slots[index] = (key, value)
                self.order.append(key)
                return

            stored_key, _ = slot
            if stored_key == key:
                self.slots[index] = (key, value)
                return

            index = (index + 1) % self.capacity
        raise MemoryError("HashTable is full!")

    def __getitem__(self, key):
        index = self._get_index(key)
        for _ in range(self.capacity):
            slot = self.slots[index]

            if slot is self._BLANK:
                raise KeyError(f"Key '{key}' not found")

            if slot is self._DELETED:
                index = (index + 1) % self.capacity
                continue

            stored_key, stored_value = slot
            if stored_key == key:
                return stored_value

            index = (index + 1) % self.capacity
        raise KeyError(f"Key '{key}' not found")

    def __delitem__(self, key):
        index = self._get_index(key)
        for _ in range(self.capacity):
            slot = self.slots[index]

            if slot is self._BLANK:
                raise KeyError(f"Key '{key}' not found")

            if slot is self._DELETED:
                index = (index + 1) % self.capacity
                continue

            stored_key, _ = slot
            if stored_key == key:
                self.slots[index] = self._DELETED
                self.order.remove(key)
                self._shrink_check()
                return

            index = (index + 1) % self.capacity
        raise KeyError(f"Key '{key}' not found")

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key, default=None):
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            return default

    def update(self, other):
        for key, value in other.items():
            self[key] = value

    def setdefault(self, key, default=None):
        if key in self:
            return self[key]
        self[key] = default
        return default

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def _shrink_check(self):
        load_factor = len(self) / self.capacity
        if load_factor <= 0.2 and self.capacity > 10:
            self._resize(self.capacity // 2)

    def clear(self):
        self.slots = [self._BLANK] * self.capacity
        self.order = []

    def _resize(self,new_capacity = None):
        if new_capacity is None:
            new_capacity = self.capacity * 2

        old_slots = self.slots
        self.capacity = new_capacity
        self.slots = [self._BLANK] * self.capacity

        for slot in old_slots:
            if slot is not self._BLANK and slot is not self._DELETED:
                key, value = slot
                index = self._get_index(key)
                while self.slots[index] is not self._BLANK:
                    index = (index + 1) % self.capacity
                self.slots[index] = (key, value)

    def items(self):
        for key in self.order:
            yield key, self[key]

    def keys(self):
        for key in self.order:
            yield key

    def values(self):
        for key in self.order:
            yield self[key]

    def __len__(self):
        return len(self.order)

    def __iter__(self):
        for key in self.order:
            yield key

    def __str__(self):
        pairs = [f"{k!r}: {v!r}" for k, v in self.items()]
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self):
        pairs = [f"{k!r}: {v!r}" for k, v in self.items()]
        return f"HashTable({'{' + ', '.join(pairs) + '}'})"

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, HashTable):
            return False
        return sorted(self.items()) == sorted(other.items())

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        if capacity is None:
            capacity = max(10, len(dictionary) * 2)
        ht = cls(capacity)
        for key, value in dictionary.items():
            ht[key] = value
        return ht



if __name__ == "__main__":
    ht = HashTable()
    for i in range(8):
        ht[f"key{i}"] = i
        print(f"count={len(ht)} capacity={ht.capacity}")

    print("---")

    for i in range(6):
        del ht[f"key{i}"]
        print(f"count={len(ht)} capacity={ht.capacity}")