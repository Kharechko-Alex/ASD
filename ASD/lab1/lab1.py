from random import uniform
from time import perf_counter
import matplotlib.pyplot as plt


def main():
    size = (10, 100, 1000, 5000, 10000, 20000, 50000)
    for i in size:
        a = [round(uniform(0, 100), 4) for _ in range(i)]
        text_info(a, i)
        plot_building(i, a)


def plot_building(size, a):
    plt.title('Bubble sort')
    plt.ylabel('Operations')
    plt.xlabel('Array size')
    x_axis = []
    y_axis = [[], [], []]

    for i in range(1, size + 1):
        arr = gen_arr(i)
        x_axis.append(i)
        y_axis[0].append(bubble_sort(arr[:])[1] + bubble_sort(arr[:])[2])
        y_axis[1].append(bubble_sort(sorted(arr[:]))[1] + bubble_sort(sorted(arr[:]))[2])
        y_axis[2].append(bubble_sort(sorted(arr[:], reverse=True))[1] + bubble_sort(sorted(arr[:], reverse=True))[2])

    plt.plot(x_axis, y_axis[0], color='red')
    plt.plot(x_axis, y_axis[1], color='green')
    plt.plot(x_axis, y_axis[2], color='purple')
    plt.plot(x_axis, [i - 1 for i in range(1, size + 1)], color='yellow', linewidth=2)
    # plt.plot(x_axis, [i ** 2 for i in range(1, size + 1)], color='blue')
    plt.legend(("randomized", "sorted", "reversed", "best variant", "worst variant"))
    plt.show()

    # plot for upgraded bubble sort
    plt.title('Upgraded Bubble sort')
    plt.ylabel('Operations')
    plt.xlabel('Array size')
    x_axis = []
    y_axis = [[], [], []]

    for i in range(1, size + 1):
        arr = gen_arr(i)
        x_axis.append(i)
        y_axis[0].append(upgraded_bubble_sort(arr[:])[1] + upgraded_bubble_sort(arr[:])[2])
        y_axis[1].append(upgraded_bubble_sort(sorted(arr[:]))[1] + upgraded_bubble_sort(sorted(arr[:]))[2])
        y_axis[2].append(
            upgraded_bubble_sort(sorted(arr[:], reverse=True))[1] + upgraded_bubble_sort(sorted(arr[:], reverse=True))[
                2])

    plt.plot(x_axis, y_axis[0], color='red')
    plt.plot(x_axis, y_axis[1], color='green')
    plt.plot(x_axis, y_axis[2], color='purple')
    plt.plot(x_axis, [i - 1 for i in range(1, size + 1)], color='yellow', linewidth=2)
    # plt.plot(x_axis, [i ** 2 for i in range(1, size + 1)], color='blue')
    plt.legend(("randomized", "sorted", "reversed", "best variant", "worst variant"))
    plt.show()

    # plot for insertion sort algorithm
    plt.title('Insertion sort')
    plt.ylabel('Operations')
    plt.xlabel('Array size')
    x_axis = []
    y_axis = [[], [], []]

    for i in range(1, size + 1):
        arr = gen_arr(i)
        x_axis.append(i)
        y_axis[0].append(insertion_sort(arr[:])[1] + insertion_sort(arr[:])[2])
        y_axis[1].append(insertion_sort(sorted(arr[:]))[1] + insertion_sort(sorted(arr[:]))[2])
        y_axis[2].append(
            insertion_sort(sorted(arr[:], reverse=True))[1] + insertion_sort(sorted(arr[:], reverse=True))[2])

    plt.plot(x_axis, y_axis[0], color='red')
    plt.plot(x_axis, y_axis[1], color='green')
    plt.plot(x_axis, y_axis[2], color='purple')
    plt.plot(x_axis, [i - 1 for i in range(1, size + 1)], color='yellow', linewidth=2)
    # plt.plot(x_axis, [i ** 2 for i in range(1, size + 1)], color='blue')
    plt.legend(("randomized", "sorted", "reversed", "best variant", "worst variant"))
    plt.show()


def text_info(a, i):
    print(f"Random generated array FOR LEN {i}: \n", a, i)
    # print("Sorted array: ")
    # print(bubble_sort(a[:])[0], end='\n\n')

    start = perf_counter()
    print(f"Sorted time for Bubble function on random array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", bubble_sort(a[:])[1])
    print("Number of permutation: ", bubble_sort(a[:])[2], end='\n\n')
    start = perf_counter()
    # print(bubble_sort(sorted(a[:]))[0])
    print(f"Sorted time for Bubble function on full-sorted array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", bubble_sort(sorted(a[:]))[1])
    print("Number of permutation: ", bubble_sort(sorted(a[:]))[2], end='\n\n')
    start = perf_counter()
    # print(bubble_sort(sorted(a[:], reverse=True))[0])
    print(f"Sorted time for Bubble function on reversed-sorted array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", bubble_sort(sorted(a[:], reverse=True))[1])
    print("Number of permutation: ", bubble_sort(sorted(a[:], reverse=True))[2], end='\n\n')

    print("\n------------------------------------------\n")

    start = perf_counter()
    # print(upgraded_bubble_sort(a[:]))
    print(f"Sorted time for Upgraded Bubble function on random array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", upgraded_bubble_sort(a[:])[1])
    print("Number of permutation: ", upgraded_bubble_sort(a[:])[2], end='\n\n')
    start = perf_counter()
    # print(upgraded_bubble_sort(sorted(a[:]))[0])
    print(f"Sorted time for Upagraded Bubble sort function on full-sorted array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", upgraded_bubble_sort(sorted(a[:]))[1])
    print("Number of permutation: ", upgraded_bubble_sort(sorted(a[:]))[2], end='\n\n')
    start = perf_counter()
    # print(upgraded_bubble_sort(sorted(a[:], reverse=True))[0])
    print(f"Sorted time for Upgraded Bubble sort function on reversed-sorted array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", upgraded_bubble_sort(sorted(a[:], reverse=True))[1])
    print("Number of permutation: ", upgraded_bubble_sort(sorted(a[:], reverse=True))[2], end='\n\n')

    print("\n------------------------------------------\n")

    start = perf_counter()
    # print(insertion_sort(a[:]))
    print(f"Sorted time for Insertion sort function on random array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", insertion_sort(a[:])[1])
    print("Number of permutation: ", insertion_sort(a[:])[2], end='\n\n')
    start = perf_counter()
    # print(insertion_sort(sorted(a[:]))[0])
    print(f"Sorted time for Insertion sort function on full-sorted array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", insertion_sort(sorted(a[:]))[1])
    print("Number of permutation: ", insertion_sort(sorted(a[:]))[2], end='\n\n')
    start = perf_counter()
    # print(insertion_sort(sorted(a[:], reverse=True))[0])
    print(f"Sorted time for Insertion sort function on reversed-sorted array: \n{perf_counter() - start} sec")
    print("Number of comprasion: ", insertion_sort(sorted(a[:], reverse=True))[1])
    print("Number of permutation: ", insertion_sort(sorted(a[:], reverse=True))[2], end='\n\n')


def gen_arr(len):
    return [uniform(-10, 10) for _ in range(len)]


def bubble_sort(list_a):
    number_of_comparison = 0
    number_of_permutation = 0

    for i in range(len(list_a) - 1):

        for j in range(len(list_a) - i - 1):

            number_of_comparison += 1
            if list_a[j] > list_a[j + 1]:
                number_of_permutation += 1
                list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]
    return list_a, number_of_comparison, number_of_permutation


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

    return array, number_of_comparison, number_of_permutation


def insertion_sort(array):
    number_of_comparison = 0
    number_of_permutation = 0
    for i in range(1, len(array)):

        key = array[i]

        j = i - 1
        while j >= 0 and (number_of_comparison := number_of_comparison + 1) and key < array[j]:
            array[j + 1] = array[j]
            number_of_permutation += 1
            j -= 1
        array[j + 1] = key

    return array, number_of_comparison, number_of_permutation


if __name__ == "__main__":
    main()
