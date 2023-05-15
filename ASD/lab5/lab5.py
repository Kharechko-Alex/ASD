import sys
import math


class Heap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return math.floor((index - 1) / 2)

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def write_data(self, data):
        for i in data:
            self.insert(i)

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)

    def parent(self, index):
        return self.heap[self.get_parent_index(index)]

    def left_child(self, index):
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up()

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_item
            self.heapify_down()
        return min_item

    def heapify_up(self):
        index = len(self.heap) - 1
        while self.has_parent(index) and self.parent(index) > self.heap[index]:
            parent_index = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.heap[index] < self.heap[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)
            index = smaller_child_index

    def display(self):
        rows = math.ceil(math.log2(len(self.heap) + 1))
        last_row_elem = 2 ** rows - 1
        index = 0
        row = 0
        while row < rows:
            elements_in_row = min(2 ** row, len(self.heap) - index)
            offset = " " * ((last_row_elem - elements_in_row) // 2)
            row_elements = []
            for j in range(elements_in_row):
                row_elements.append(str(self.heap[index]))
                index += 1
            print(offset + "  ".join(row_elements))
            row += 1

    def sort(self):
        sorted_heap = []
        while self.heap:
            sorted_heap.append(self.extract_min())
        return sorted_heap

    def remove(self, item):
        if item not in self.heap:
            raise ValueError("Item not found in the heap")
        item_index = self.heap.index(item)
        last_item = self.heap.pop()
        if item_index < len(self.heap):
            self.heap[item_index] = last_item
            if self.has_parent(item_index) and self.parent(item_index) > self.heap[item_index]:
                self.heapify_up()
            else:
                self.heapify_down()


def take_res(data):
    array = []
    for i in range(len(data)):
        median = []
        part_data = data[:i + 1]
        root = Heap()
        root.write_data(part_data)
        # root.display()
        sorted_arr = root.sort()
        # print(sorted_arr)
        if len(sorted_arr) % 2 == 0:
            median.append(sorted_arr[len(sorted_arr) // 2])
            median.append(sorted_arr[len(sorted_arr) // 2 - 1])
        else:
            median.append(sorted_arr[len(sorted_arr) // 2])
        # root.display()
        array.append(sorted(median))
    return array


def write(res):
    with open('ip24_kharechko_output.txt', 'w') as f:
        for i in range(len(res)):
            f.write('\n' + ' '.join(map(str, res[i])))


def main():
    y = str(sys.argv[1])
    with open(f'data\{y}', 'r') as f:
        data = [int(line.strip()) for line in f.readlines()[1:]]
    result = take_res(data)
    write(result)


if __name__ == "__main__":
    main()
