from random import uniform
from time import perf_counter


def main():
    a = [round(uniform(-10, 10), 4) for _ in range(1000)]
    print("Random generated array: \n", a)
    start = perf_counter()
    print(bubble_sort(a[:]))
    print(f"Sorted time for Bubble function on random array: \n{perf_counter()-start} sec")

    start = perf_counter()
    print(bubble_sort(sorted(a[:])))
    print(f"Sorted time for Bubble function on full-sorted array: \n{perf_counter()-start} sec")

    start = perf_counter()
    print(bubble_sort(sorted(a[:], reverse = True)))
    print(f"Sorted time for Bubble function on reversed-sorted array: \n{perf_counter()-start} sec")
    print("\n------------------------------------------\n")

    start = perf_counter()
    print(upgraded_bubble_sort(a[:]))
    print(f"Sorted time for Upgraded Bubble function: {perf_counter()-start} sec")
    print("\n------------------------------------------\n")
    start = perf_counter()
    print(insertion_sort(a[:]))
    print(f"Sorted time for insertion sort function: {perf_counter()-start} sec")


def bubble_sort(list_a):
    number_of_comparison = 0
    number_of_permutation = 0

    for i in range(len(list_a)-1):

        for j in range(len(list_a) - i - 1):

            number_of_comparison += 1
            if list_a[j] > list_a[j+1]:
                number_of_permutation += 1
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
    print()
    return list_a


def upgraded_bubble_sort(array):
    number_of_comparison = 0
    number_of_permutation = 0
    for i in range(len(array)):

        swapped = False

        for j in range(0, len(array) - i - 1):
            number_of_comparison += 1

            if array[j] > array[j + 1]:
                number_of_permutation += 1
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if swapped == False:
            break

    return array


def insertion_sort(array):
    number_of_comparison = 0
    number_of_permutation = 0
    for i in range(1, len(array)):

        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            number_of_comparison += 1
            array[j + 1] = array[j]
            number_of_permutation += 1
            j -= 1
        array[j + 1] = key

    return array



if __name__ == "__main__":
    main()
