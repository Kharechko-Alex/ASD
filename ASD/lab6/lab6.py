import random
import string
import matplotlib.pyplot as plt
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def fnv32(self, key):
        # Хеш-функція FNV-32
        fnv_prime = 16777619
        fnv_offset_basis = 2166136261
        hash_value = fnv_offset_basis
        # "a" -> 65

        for char in key:
            hash_value ^= ord(char)
            hash_value *= fnv_prime
            hash_value &= 0xffffffff  # Забезпечення 32-бітного значення
        return hash_value



    def search(self, key):
        comparison = 0
        index = self.fnv32(key) % self.size
        chain = self.table[index]
        for item in chain:
            comparison += 1
            if item[0] == key:
                return item[1], comparison
        return None, comparison

    def insert(self, key, value):
        index = self.fnv32(key) % self.size
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                item[1].add(value)  # Оновлення значення, якщо ключ вже існує
                return
        chain.append([key, value])  # Додавання нової пари ключ-значення

def generate_random_string(length):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def plotting(length):
    graph_data = []
    key_arr = []
    for size in range(length):
        for _ in range(length):
            key_arr.append(generate_random_string(10))
        hash_table = HashTable(size+1)
        for key in key_arr:
            value = generate_random_string(40)
            hash_table.insert(key, value)
        graph_data.append(hash_table.search(key_arr[-1])[1])
        print(size)
    plt.title('Hash_table')
    plt.ylabel('Comparisons')
    plt.xlabel('Size')
    plt.plot(range(1, length + 1), graph_data, color='b')
    plt.show()


num_arr = [100, 1000, 5000, 10000, 20000]

for num in num_arr:
    hash_table = HashTable(num)
    key_arr =[]
    for i in range(num):
        key_arr.append(generate_random_string(10))

    for key in key_arr:
        value = generate_random_string(40)
        hash_table.insert(key, value)
        print("|", key, "|", hash_table.search(key)[0], "|")
    plotting(num)
    print(f"\nNUMBER LEN {num}\n")
    print("="*200)

