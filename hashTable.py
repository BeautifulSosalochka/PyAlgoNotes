class HashTable:
    """
    A simple implementation of a hash table with basic operations: insert, search, and delete.
    """
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Compute the hash value for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hashed_key].append([key, value])

    def search(self, key):
        """Search for a value by its key."""
        hashed_key = self._hash(key)
        for pair in self.table[hashed_key]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        hashed_key = self._hash(key)
        for i, pair in enumerate(self.table[hashed_key]):
            if pair[0] == key:
                del self.table[hashed_key][i]
                return True
        return False

    def display(self):
        """Display the current state of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


def test_hash_table():
    ht = HashTable(size=10)

    # Insert some key-value pairs
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("orange", 300)
    ht.insert("grape", 400)

    print("Hash Table:")
    ht.display()

    print("\nSearch results:")
    print("apple:", ht.search("apple"))
    print("banana:", ht.search("banana"))
    print("pear:", ht.search("pear"))

    print("\nDeleting 'banana'...")
    ht.delete("banana")

    print("Hash Table after deletion:")
    ht.display()


# Example usage
if __name__ == "__main__":
    test_hash_table()
