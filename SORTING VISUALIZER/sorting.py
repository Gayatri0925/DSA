import matplotlib.pyplot as plt
import random
import time

# Visualizer function with color gradient
def visualize(arr, sorted_idx=None, color_positions=[], title="Sorting Visualizer"):
    plt.clf()
    colors = []
    for i in range(len(arr)):
        if i in color_positions:
            colors.append('orange')  # elements being compared
        elif sorted_idx is not None and i <= sorted_idx:
            colors.append('green')   # sorted elements
        else:
            colors.append('skyblue') # unsorted elements
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.pause(0.3)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            visualize(arr, sorted_idx=n-i-1, color_positions=[j, j+1], title=f"Bubble Sort Step {i}-{j}")

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            visualize(arr, sorted_idx=i-1, color_positions=[i, j, min_idx], title=f"Selection Sort Step {i}-{j}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualize(arr, sorted_idx=i, color_positions=[i, min_idx], title=f"Selection Swap {i}")

# Merge Sort
def merge_sort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        visualize(arr, sorted_idx=k-1, color_positions=[k], title="Merge Sort Merging")
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        visualize(arr, sorted_idx=k-1, color_positions=[k], title="Merge Sort Merging")
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        visualize(arr, sorted_idx=k-1, color_positions=[k], title="Merge Sort Merging")
        k += 1

# Quick Sort
def quick_sort(arr, low=0, high=None, sorted_idx=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    elif sorted_idx is not None:
        visualize(arr, sorted_idx=sorted_idx, title="Quick Sort Sorted")

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        visualize(arr, color_positions=[i, j, high], title="Quick Sort Partitioning")
    arr[i+1], arr[high] = arr[high], arr[i+1]
    visualize(arr, color_positions=[i+1, high], title="Quick Sort Swap Pivot")
    return i + 1

# Main function
def main():
    arr = [random.randint(1, 50) for _ in range(15)]
    print("Original Array:", arr)

    plt.ion()  # interactive mode on
    visualize(arr, title="Original Array")

    print("Choose sorting algorithm:\n1. Bubble Sort\n2. Selection Sort\n3. Merge Sort\n4. Quick Sort")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        bubble_sort(arr)
    elif choice == '2':
        selection_sort(arr)
    elif choice == '3':
        merge_sort(arr)
    elif choice == '4':
        quick_sort(arr)
    else:
        print("Invalid choice!")
        return

    visualize(arr, sorted_idx=len(arr)-1, title="Sorted Array")
    plt.ioff()
    plt.show()
    print("Sorted Array:", arr)

if __name__ == "__main__":
    main()
