import random
import time

def bubble_sort(my_list):
    n = len(my_list)

    for i in range(n-1):
        swapped = False
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                swapped = True
        if not swapped:
            break
    return my_list

def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        min_elem = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_elem]:
                min_elem = j
        my_list[i], my_list[min_elem] = my_list[min_elem], my_list[i]

    return my_list

def insertion_sort(my_list):
    n = len(my_list)

    for i in range(1, n):
        key = my_list[i]
        j = i-1

        while j >= 0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j-=1
        my_list[j+1] = key
    return my_list

def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[len(my_list)//2]
    left = [x for x in my_list if x < pivot]
    middle = [x for x in my_list if x == pivot]
    right = [x for x in my_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1

    return my_list

def generate_numbers(n):
    random_list = []
    for _ in range(n):
        random_list.append(random.randint(1, 100))
    return random_list

def timer_func(algorithm, list):
    # --- Time Measurement ---
    # Record the starting time
    start_time = time.perf_counter()
    # Run the algorithm you want to time
    algorithm(list)
    # Record the ending time
    end_time = time.perf_counter()  # Record the ending time
    # Calculate the difference to get the execution time
    execution_time = end_time - start_time
    return execution_time

my_list = generate_numbers(8000)
copy1, copy2, copy3, copy4, copy5 = my_list.copy(), my_list.copy(), my_list.copy(), my_list.copy(), my_list.copy()

time_bubble = timer_func(bubble_sort, copy1)
time_selection = timer_func(selection_sort, copy2)
time_insertion = timer_func(insertion_sort, copy3)
time_quick = timer_func(quick_sort, copy4)
time_merge = timer_func(merge_sort, copy5)

print("\nSorting algorithm           Time")
print("------------------------      -----------")
print(f"{'Bubble sort':<25}{time_bubble:.3f}")
print(f"{'Selection sort':<25}{time_selection:.3f}")
print(f"{'Insertion sort':<25}{time_insertion:.3f}")
print(f"{'Quick sort':<25}{time_quick:.3f}")
print(f"{'Merge sort':<25}{time_merge:.3f}")

print("\nAnswer to the Question: The fastest sorting algorithm is the Quick sort and the slowest is the Bubble sort")
