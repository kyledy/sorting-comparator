# A project that compares sorting algorithms and their running times in Python. 

import random
import time
import sys

# Bubble Sort
# Sorts the array in ascending order by repeatedly swapping adjacent elements until the array is sorted.
# Average-case Time Complexity: O(n^2) 
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

# Insertion Sort
# The list is divided into two parts: a sorted and unsorted part. At each stage of the iteration, an element is picked from the unsorted part
# and inserted into the correct position in the sorted part.
# Average-case Time Complexity: O(n^2), but generally faster
def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        temp = list[i]
        j = i-1
        while j >=0 and temp < list[j] :
                list[j + 1] = list[j]
                j -= 1
        list[j + 1] = temp
    return list

# Selection Sort 
# Like Insertion Sort, this algorithm divides a list into a sorted and unsorted portion. Selection sort repeatedly selects the smallest element from the
# unsorted portion and swaps it with the first element of the first element of the unsorted portion. This continues until the array is sorted.
# Average case Time Complexity: O(n^2)
def selection_sort(list):
    n = len(list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

# Quick Sort
# Quick sort divides the list into elements that are less than the pivot and elements that are greater than the pivot. In this implementation, the pivot is selected as the last element in the list. The pivot is then
# placed in its correct position in the list and the index of this position is returned. 
# Average-case Time Complexity: O(n*logn)
def quick_sort(list, low, high):
    n = len(list)
    if low < high:
        pi = partition(list, low, high)
        quick_sort(list, low, pi-1)
        quick_sort(list, pi+1, high)
    return list

# Helper function for Quick Sort
def partition(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return i + 1

# Merge Sort
# Merge sort divides the list into two equal halves, then sorts it recursively by taking the comparing elements from each half and adding the smaller of the two to the final list until both lists are processed.
# Average-case Time Complexity: O(n*logn)
def merge_sort(list):
    n = len(list)
    if n > 1:
        mid = n // 2
        L = list[:mid]
        R = list[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
    return list

# Heap Sort
# Heap sort first takes an array and builds it into a max heap. It then repeatedly swaps the first and last elements of the heap and calls "heapify" until all elements are sorted.
# Average-case Time Complexity: O(n*logn)
def heap_sort(list):
    n = len(list)
    for i in range(n, -1, -1):
        heapify(list, n, i)
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)
    return list

# Helper function for Heap Sort
def heapify(list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and list[i] < list[l]:
        largest = l
    if r < n and list[largest] < list[r]:
        largest = r
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)

# Radix Sort
# Radix sort takes an input list and uses its least significant digit as a key for sorting. It uses the maximum value and the number of digits in the list and uses it to determine the total number of iterations.
# It then sorts the value into 10 buckets based on the value of the digit. It then concatenates these buckets to produce the sorted list.
# Average-case Time Complexity: O(d*(n+10)) where d is the number of digits in the given list, and n is the number of elements. 
def radix_sort(list):
    max_value = max(list)
    max_digit = len(str(max_value))
    mod = 10
    div = 1
    while max_digit > 0:
        bucket = [[] for _ in range(10)]
        for num in list:
            digit = (num % mod) // div
            bucket[digit].append(num)
        i = 0
        for b in bucket:
            for num in b:
                list[i] = num
                i += 1
        mod *= 10
        div *= 10
        max_digit -= 1
    return list


# Counting Sort
# Counting sort uses an array 'count' to keep track of the frequency of every value in the list. It then uses the array to determine its final position in the sorted list.
# Average-case Time Complexity: O(n+k) where n is the number of elements and k is the range of the elements
def counting_sort(list):
    max_value = max(list)
    m = max_value + 1
    count = [0] * m
    for l in list:
        count[l] += 1
    i = 0
    for l in range(m):
        for c in range(count[l]):
            list[i] = l
            i += 1
    return list


# Shell Sort
# Shell sort is a variation on the insertion sort algorithm. It uses a gap value to control the size of each sublist. The gap value is initially set to half of the list, which is divided by 2 with each successive iteration.
# It then performs insertion sort on each of the sublists created by the gap.
# Average-case Time Complexity: O(n*logn^2) or O(n^(3/2))
def shell_sort(list):
    n = len(list)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = list[i]
            j = i
            while j >= gap and list[j-gap] > temp:
                list[j] = list[j-gap]
                j -= gap
            list[j] = temp
        gap //= 2
    return list


# Bucket Sort
# Bucket sort uses a 'bucket' array to store the frequency of every value in the list. It then uses this array to find the final position of the value in the sorted array.
# Average-case Time Complexity: O(n+k) where n is the number of elements and k is the number of buckets. 
def bucket_sort(list):
    n = len(list)
    max_value = max(list)
    size = max_value + 1
    bucket = [0] * size
    for i in range(n):
        bucket[list[i]] += 1
    j = 0
    for i in range(size):
        for _ in range(bucket[i]):
            list[j] = i
            j += 1
    return list


# Helper function to compute the time of a particular sorting algorithm
def get_sorting_time(algo, list):
    listCpy = list # So that the original list isn't modified
    # The time module can't process time that takes less than a second, so I have to increase the running time by a noticeable degree.
    start_time = time.time()
    for i in range(10000):
        algo(listCpy)
    end_time = time.time()
    total_time = end_time - start_time
    return str(round(total_time * 10, 3))

# Helper function for debugging 
def make_random_list():
    list = []
    for i in range(10):
        number = random.randint(1, 100)
        list.append(number)
    return list

# Driver code 
def main():
    print("\n")
    print("Welcome to the Sorting Algorithm Comparator.")

    # Generates a random list of 10 numbers from 1-100 
    list = []
    for i in range(10):
       number = random.randint(1, 100)
       list.append(number)
    
    # uses built-in function in python
    sorted_list = sorted(list)
    print("Your list is: " + str(list))
    print("The sorted list is: " + str(sorted_list))
    print("\n")

    while True:
        consent = input("Type in R to run the comparator, or Q to quit: ")
        if consent.upper() != "R" and consent.upper() != "Q":
            print("That was not a valid input. Please try again.")
            print("\n")
        elif consent.upper() == "Q":
            print("Thank you for using the Algorithm Comparator!")
            sys.exit()
        else:
            break

    print("------------------------------------------------")

    # Bubble Sort
    bblTime = get_sorting_time(bubble_sort, list)
    print("Bubble Sort: " + bblTime  + " s")

    print("------------------------------------------------")

    # Insertion Sort 
    insertionTime = get_sorting_time(insertion_sort, list)
    print("Insertion Sort: " + insertionTime + " s")

    print("------------------------------------------------")

    # Selection Sort 
    selectionTime = get_sorting_time(selection_sort, list)
    print("Selection Sort: " + selectionTime + " s")

    print("------------------------------------------------")

    # Quick Sort 
    # Special case as Quick Sort is recursive and requires more than one input.
    listCpy = list
    start_time = time.time()
    n = len(listCpy)
    for i in range(10000):
        quick_sort(listCpy, 0, n-1)
    end_time = time.time()
    total_time = end_time - start_time
    quickTime = str(round(total_time * 10, 3))
    print("Quick Sort: " + quickTime + " s") 

    print("------------------------------------------------")

    # Merge Sort
    mergeTime = get_sorting_time(merge_sort, list)
    print("Merge Sort: " + mergeTime + " s") 
    
    print("------------------------------------------------")

    # Heap Sort
    heapTime = get_sorting_time(heap_sort, list)
    print("Heap Sort: " + heapTime + " s") 
    
    print("------------------------------------------------")

    # Radix Sort
    radixTime = get_sorting_time(radix_sort, list)
    print("Radix Sort: " + radixTime + " s") 

    print("------------------------------------------------")

    # Counting Sort
    countingTime = get_sorting_time(counting_sort, list)
    print("Counting Sort: " + countingTime + " s") 
    
    print("------------------------------------------------")

    # Shell Sort
    shellTime = get_sorting_time(shell_sort, list)
    print("Shell Sort: " + shellTime + " s") 
    
    print("------------------------------------------------")

    # Bucket Sort
    bucketTime = get_sorting_time(bucket_sort, list)
    print("Bucket Sort: " + bucketTime + " s") 

    print("------------------------------------------------")
    print("Thank you for using the Algorithm Comparator!")
    print("\n")

main()