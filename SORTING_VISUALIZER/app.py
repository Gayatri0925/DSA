import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

st.set_page_config(page_title="Sorting Visualizer", page_icon="📊", layout="wide")

# --- Visualization Function ---
def visualize(arr, color_positions=[], sorted_idx=None, title="Sorting Visualizer"):
    colors = []
    for i in range(len(arr)):
        if i in color_positions:
            colors.append("orange")  # currently comparing
        elif sorted_idx is not None and i <= sorted_idx:
            colors.append("green")   # sorted
        else:
            colors.append("skyblue") # unsorted
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color=colors)
    ax.set_title(title)
    st.pyplot(fig)
    time.sleep(0.3)

# --- Sorting Algorithms ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            visualize(arr, color_positions=[j, j + 1], sorted_idx=n - i - 1, title=f"Bubble Sort Step {i}-{j}")

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            visualize(arr, color_positions=[i, j, min_idx], sorted_idx=i - 1, title=f"Selection Sort Step {i}-{j}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        visualize(arr, color_positions=[i, min_idx], sorted_idx=i, title=f"Selection Sort Swap {i}")

def merge(arr, l, m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        visualize(arr, color_positions=[k], sorted_idx=k - 1, title="Merge Sort Merging")
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        visualize(arr, color_positions=[k], sorted_idx=k - 1, title="Merge Sort Merging")
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        visualize(arr, color_positions=[k], sorted_idx=k - 1, title="Merge Sort Merging")
        k += 1

def merge_sort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        visualize(arr, color_positions=[i, j, high], title="Quick Sort Partitioning")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    visualize(arr, color_positions=[i + 1, high], title="Quick Sort Pivot Swap")
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# --- Streamlit UI ---
st.title("📊 Sorting Algorithm Visualizer")
st.markdown("### Watch how sorting algorithms arrange elements step by step!")

algo = st.selectbox("Choose an algorithm:", ["Bubble Sort", "Selection Sort", "Merge Sort", "Quick Sort"])
size = st.slider("Array size:", 5, 30, 15)
arr = [random.randint(1, 50) for _ in range(size)]

st.write("### Original Array:")
st.bar_chart(arr)

if st.button("Start Visualization 🚀"):
    temp_arr = arr.copy()
    if algo == "Bubble Sort":
        bubble_sort(temp_arr)
    elif algo == "Selection Sort":
        selection_sort(temp_arr)
    elif algo == "Merge Sort":
        merge_sort(temp_arr)
    elif algo == "Quick Sort":
        quick_sort(temp_arr)

    st.success("✅ Sorting Completed!")
    st.write("### Sorted Array:")
    st.bar_chart(temp_arr)
