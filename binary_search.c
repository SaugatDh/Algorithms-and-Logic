#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 1. Changed index parameters to size_t (64-bit) and array values to long long
size_t binary_search(const long long *arr, size_t size, long long targetValue, int *count) {
    size_t left = 0;
    size_t right = size - 1;
    *count = 0;

    // Use a standard safety flag because size_t is unsigned and cannot go below 0
    while (left <= right) {
        (*count)++;
        size_t mid = left + (right - left) / 2;

        if (arr[mid] == targetValue) {
            return mid;
        }
        if (arr[mid] < targetValue) {
            left = mid + 1;
        } else {
            // Unsigned underflow guard: if mid is 0 and target is smaller, it's not found
            if (mid == 0) break; 
            right = mid - 1;
        }
    }
    return -1; // Returns (size_t)-1, which acts as an error state
}

int main() {
    // 2. size_t ensures safe allocation math for sizes > 2 billion items
    // 1 Billion elements of 8-byte long longs = ~8 Gigabytes of RAM
    const size_t LIST_SIZE = 1000000000; 
    long long target = 44;
    int total_turns = 0;

    clock_t start_creation = clock();

    // 3. Allocating 64-bit integer blocks on the heap
    long long *my_list = (long long *)malloc(LIST_SIZE * sizeof(long long));
    if (my_list == NULL) {
        printf("Memory allocation failed! Your system ran out of RAM.\n");
        return 1;
    }
    
    for (size_t i = 0; i < LIST_SIZE; i++) {
        my_list[i] = (long long)i;
    }

    clock_t end_creation = clock();

    clock_t start_search = clock();
    size_t result = binary_search(my_list, LIST_SIZE, target, &total_turns);
    clock_t end_search = clock();

    double creation_time = (double)(end_creation - start_creation) / CLOCKS_PER_SEC;
    double search_time = (double)(end_search - start_search) / CLOCKS_PER_SEC;

    printf("List creation time: %.6f seconds\n", creation_time);
    printf("Binary search time: %.8f seconds\n", search_time);

    // 4. Using %zu formatter for size_t and %lld for long long
    if (result != (size_t)-1) {
        printf("Found at index %zu in %d turn(s) for %zu elements.\n", result, total_turns, LIST_SIZE);
    } else {
        printf("Target %lld not found.\n", target);
    }

    free(my_list);
    return 0;
}
