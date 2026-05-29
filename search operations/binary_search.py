import time

# 1. Start the clock for list creation
start_creation = time.perf_counter()
my_list = list(range(1000))
end_creation = time.perf_counter()

x = 44

def binary_search(arr, targetValue):
    left = 0
    count = 0
    right = len(arr) - 1

    while left <= right:
        count += 1
        mid = (left + right) // 2
        if arr[mid] == targetValue:
            return mid, count
        if arr[mid] < targetValue:
            left = mid + 1
        else:
            right = mid - 1
    return -1, count

# 2. Start the clock for binary search
start_search = time.perf_counter()
result, total_turns = binary_search(my_list, x)
end_search = time.perf_counter()

# 3. Print the results and metrics
creation_time = end_creation - start_creation
search_time = end_search - start_search

print(f"List creation time: {creation_time:.8f} seconds")
print(f"Binary search time: {search_time:.8f} seconds")

if result != -1:
    print(f"Found at index {result} in {total_turns} turn(s).")
else:
    print(result)
