class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def delete(self, key):
        if key in self.table:
            del self.table[key]

    def search(self, key):
        if key in self.table:
            return self.table[key]
        else:
            return None

 
hash_table = HashTable()
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.delete("key1")
print(hash_table.search("key2")) # Output: value2




class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        if key in self.table:
             
            self.table[key].append(value)
        else:
             
            self.table[key] = [value]

    def delete(self, key):
        if key in self.table:
            # if the key exists in the hash table, remove the entire linked list
            del self.table[key]

    def search(self, key):
        if key in self.table:
            # if the key exists in the hash table, return the entire linked list
            return self.table[key]
        else:
            # if the key doesn't exist in the hash table, return None
            return None


hash_table = HashTable()
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key1", "value3") # add another value to the linked list for key1
print(hash_table.search("key1")) # Output: ['value1', 'value3']
hash_table.delete("key1")
print(hash_table.search("key1")) # Output: None
