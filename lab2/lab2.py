import time
import matplotlib.pyplot as plt
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
    if len(arr) > 1:

        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


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
    swapped = False
    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


def calculate_execution_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    return end_time - start_time, sorted_arr


sizes = [x for x in range(1000, 5001, 1000)]
sort_functions = [quicksort]

sort_names = ['Quicksort']

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


