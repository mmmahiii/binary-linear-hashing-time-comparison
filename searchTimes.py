import time
import matplotlib.pyplot as plt
import numpy as np

# Define the search and retrieval functions

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

def binarySearch(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def retrieveData(array, key):
    LENGTH = len(array)
    index = hash(key) % LENGTH
    initial_index = index
    while True:
        if array[index][0] is None:
            return None
        elif array[index][1] == key:
            return array[index][0]
        else:
            index = (index + 1) % LENGTH
            if index == initial_index:
                return None

# Compute average times over multiple runs for all methods

arrays = [list(range(1, i + 1)) for i in range(1, 101)]
linear_search_avg_times = []
binary_search_avg_times = []
hash_table_retrieve_times = []

num_runs = 1000
for arr in arrays:
    # Linear and Binary Search Timing
    linear_search_run_times = []
    binary_search_run_times = []
    for _ in range(num_runs):
        search_val = len(arr) + 1
        start_time = time.time()
        linearSearch(arr, search_val)
        end_time = time.time()
        linear_search_run_times.append(end_time - start_time)

        start_time = time.time()
        binarySearch(arr, search_val)
        end_time = time.time()
        binary_search_run_times.append(end_time - start_time)
    linear_search_avg_times.append(sum(linear_search_run_times) / num_runs)
    binary_search_avg_times.append(sum(binary_search_run_times) / num_runs)

    # Hash Table Retrieval Timing
    hash_table = [[None, None] for _ in range(len(arr))]
    key = "test_key"
    data = "test_data"
    index = hash(key) % len(arr)
    hash_table[index] = [data, key]
    start_time = time.time()
    retrieveData(hash_table, key)
    end_time = time.time()
    hash_table_retrieve_times.append(end_time - start_time)

# Plotting
plt.figure(figsize=(10,6))
plt.plot(range(1, 101), linear_search_avg_times, label='Linear Search', color='blue')
plt.plot(range(1, 101), binary_search_avg_times, label='Binary Search', color='red')
plt.plot(range(1, 101), hash_table_retrieve_times, label='Hash Table Retrieval', color='green')
plt.xlabel('Data Structure Size')
plt.ylabel('Average Time (seconds)')
plt.title('Comparison of Search and Retrieval Time Complexities')
plt.legend()
plt.grid(True)
plt.show()
