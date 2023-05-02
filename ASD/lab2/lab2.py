import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])

    merged, merge_inv = merge(left, right)
    return merged, merge_inv + right_inv + left_inv


def merge(left, right):
    result = []
    inversions = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversions += len(left) - i

    result += left[i:]
    result += right[j:]
    print(inversions)
    return result, inversions


def inversion(curr, comp):
    ind = []
    for i in range(len(comp)):
        ind.append(comp[curr.index(i + 1)])
    return merge_sort(ind)


def take_res(x, data):
    array = []
    for i in range(len(data)):
        if i != x - 1:
            print("#", i + 1)
            array.append((i + 1, inversion(data[x - 1], list(data[i][j] for j in range(len(data[i]))))[1]))
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j][1] > array[j + 1][1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def write(x, res):
    with open('ip24_kharechko_' + str(x) + '_output.txt', 'w') as f:
        f.write(str(x))
        for i in range(len(res)):
            f.write('\n' + ' '.join(map(str, res[i])))


def main():
    x = int(sys.argv[2])
    y = str(sys.argv[1])
    with open(f'data\{y}', 'r') as f:
        data = [list(map(int, line.strip().split()))[1:] for line in f.readlines()[1:]]
    result = take_res(x, data)
    write(x, result)


if __name__ == "__main__":
    main()
