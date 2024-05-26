class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_index = self._hash_function(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = (key, value)
        else:
            original_hash_index = hash_index
            while self.table[hash_index] is not None:
                hash_index = (hash_index + 1) % self.size
                if hash_index == original_hash_index:
                    raise Exception("Hash table penuh")
            self.table[hash_index] = (key, value)

    def search(self, key):
        hash_index = self._hash_function(key)
        original_hash_index = hash_index
        while self.table[hash_index] is not None:
            if self.table[hash_index][0] == key:
                return self.table[hash_index][1]
            hash_index = (hash_index + 1) % self.size
            if hash_index == original_hash_index:
                break
        return None

    def delete(self, key):
        hash_index = self._hash_function(key)
        original_hash_index = hash_index
        while self.table[hash_index] is not None:
            if self.table[hash_index][0] == key:
                # Hapus elemen dengan menyetel None
                self.table[hash_index] = None
                # Rehash semua elemen setelah elemen yang dihapus
                next_index = (hash_index + 1) % self.size
                while self.table[next_index] is not None:
                    next_key, next_value = self.table[next_index]
                    self.table[next_index] = None
                    self.insert(next_key, next_value)
                    next_index = (next_index + 1) % self.size
                return
            hash_index = (hash_index + 1) % self.size
            if hash_index == original_hash_index:
                break
        print(f"Key {key} tidak ditemukan.")

    def display(self):
        for index, element in enumerate(self.table):
            if element is not None:
                print(f"{index} --> {element}")
            else:
                print(f"{index}")

if __name__ == "__main__":
    nama = "Rangga Aditya Pradana"
    nim = "064002300026"
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")

    key_pertama = int(nim[-2:])

    data = [
        (key_pertama, nama),
        (1, "Louis"),
        (14, "Grace"),
        (25, "Mark"),
        (19, "Rifdah")
    ]

    hash_table = HashTable(size=10)

    for key, value in data:
        hash_table.insert(key, value)

    hash_table.display()

    search_key = int(input("Data yang ingin dicari dengan key adalah: "))
    result = hash_table.search(search_key)
    if result:
        print(f"Data dengan key {search_key} adalah: {result}")
    else:
        print(f"Data dengan key {search_key} tidak ditemukan.")

    delete_key = int(input("Data yang ingin dihapus dengan key adalah: "))
    hash_table.delete(delete_key)
    hash_table.display()
