import time
import matplotlib.pyplot as plt
import numpy as np
import random


def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = mergesort(left)
    right_sorted = mergesort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def heapsort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n//2, -1, -1):
        heapify(sorted_arr, n, i)
    for i in range(n-1, 0, -1):
        sorted_arr[i], sorted_arr[0] = sorted_arr[0], sorted_arr[i]
        heapify(sorted_arr, i, 0)
    return sorted_arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def bubblesort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


def calculate_execution_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    return end_time - start_time, sorted_arr


def plot_graph(execution_times, labels):
    x = np.arange(len(execution_times))
    plt.bar(x, execution_times, align='center', alpha=0.5)
    plt.xticks(x, labels)
    plt.ylabel('Execution Time (s)')
    plt.title('Sorting Algorithm Execution Times')
    plt.tight_layout()
    plt.show()


sizes = [1000, 2000, 3000, 4000, 5000]
sort_functions = [quicksort, mergesort, heapsort, bubblesort]

sort_names = ['Quicksort', 'Merge Sort', 'Heap Sort', 'Bubble Sort']
execution_time = {name: [] for name in sort_names}

for s in sizes:
    array = generate_random_array(s)
    for sort_fun, name in zip(sort_functions, sort_names):
        time_taken, _ = calculate_execution_time(sort_fun, array.copy())
        execution_time[name].append(time_taken)

for name, times in execution_time.items():
    print(f"{name}: {times}")

for name, times in execution_time.items():
    plt.plot(sizes, times, label=name)

plt.xlabel('Array Size')
plt.ylabel('Execution Time (s)')
plt.title('Sorting Algorithm Execution Times')
plt.legend()
plt.show()
