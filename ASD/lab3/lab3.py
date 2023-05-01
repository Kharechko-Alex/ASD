# import sys
check1 = 0

def quick_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    for num in arr:
        if num < pivot:
            comparisons += 1
            left.append(num)
        elif num > pivot:
            comparisons += 1
            right.append(num)
    sorted_left, comparisons_left = quick_sort(left)
    sorted_right, comparisons_right = quick_sort(right)
    return sorted_left + [pivot] + sorted_right, comparisons + comparisons_left + comparisons_right


def write(x, res):
    with open('ip24_kharechko_' + str(x) + '_output.txt', 'w') as f:
        f.write(str(x))
        for i in range(len(res)):
            f.write('\n' + ' '.join(map(str, res[i])))


def main():
    # x = int(sys.argv[1])
    with open('input_05_10.txt', 'r') as f:
        data = [int(line) for line in f.readlines()][1:]
    array, comparisons = quick_sort(data)
    print(comparisons)
    print(array)


if __name__ == "__main__":
    main()
