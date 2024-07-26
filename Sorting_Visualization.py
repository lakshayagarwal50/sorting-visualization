import matplotlib.pyplot as plt
import random
import time


# Function to visualize the sorting algorithm
def visualize_sort(sort_func, arr):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title("Sorting Algorithm: {}".format(sort_func.__name__))

    start_time = time.time()  # get the current time

    # Plotting the bars for the array elements
    bars = ax.bar(range(n), arr)

    # Call the sort function once for quick_sort
    if sort_func == quick_sort:
        sort_func(arr, 0, n, bars)
    else:
        # Loop to animate the sorting process for other algorithms
        for i in range(n):
            sort_func(arr, i, n, bars)
            plt.draw()
            plt.pause(1.5)

    end_time = time.time()  # get the current time again
    time_taken = end_time - start_time  # calculate the elapsed time
    print("Time taken: {:.2f} seconds".format(time_taken))

    plt.show()


# Function to implement Bubble sort
def bubble_sort(arr, i, n, bars):
    # Loop to compare adjacent elements and swap if required
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            # Change color to red while swapping elements
            bars[j].set_color("red")
            bars[j + 1].set_color("red")
            plt.pause(0.5)
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # Update the height of the bars to reflect the change
            bars[j].set_height(arr[j])
            bars[j + 1].set_height(arr[j + 1])
            # Change color back to blue after swapping elements
            bars[j].set_color("blue")
            bars[j + 1].set_color("blue")


# Function to implement Insertion sort
def insertion_sort(arr, i, n, bars):
    key = arr[i]
    j = i - 1
    # Loop to shift elements to make space for the key element
    while j >= 0 and key < arr[j]:
        # Change color to red while shifting elements
        bars[j].set_color("red")
        bars[j + 1].set_color("red")
        plt.pause(0.5)
        arr[j + 1] = arr[j]
        # Update the height of the bars to reflect the change
        bars[j + 1].set_height(arr[j])
        j -= 1
    arr[j + 1] = key
    # Update the height of the bars to reflect the change
    bars[j + 1].set_height(key)
    # Change color back to blue after inserting the key element
    bars[j + 1].set_color("blue")


# Function to implement Selection sort
def selection_sort(arr, i, n, bars):
    min_idx = i
    # Loop to find the minimum element
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    # Change color to red while swapping elements        
    bars[i].set_color("red")
    bars[min_idx].set_color("red")
    plt.pause(0.5)
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Update the height of the bars to reflect the change
    bars[i].set_height(arr[i])
    bars[min_idx].set_height(arr[min_idx])
    bars[i].set_color("blue")
    bars[min_idx].set_color("blue")


def partition(arr, low, high, bars):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            bars[i].set_color("red")
            bars[j].set_color("red")
            plt.pause(0.5)
            arr[i], arr[j] = arr[j], arr[i]
            bars[i].set_height(arr[i])
            bars[j].set_height(arr[j])
            bars[i].set_color("blue")
            bars[j].set_color("blue")

    bars[i + 1].set_color("red")
    bars[high].set_color("red")
    plt.pause(0.5)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    bars[i + 1].set_height(arr[i + 1])
    bars[high].set_height(arr[high])
    bars[i + 1].set_color("blue")
    bars[high].set_color("blue")

    return i + 1


def quick_sort_helper(arr, low, high, bars):
    if low < high:
        pi = partition(arr, low, high, bars)

        quick_sort_helper(arr, low, pi - 1, bars)
        quick_sort_helper(arr, pi + 1, high, bars)


def quick_sort(arr, i, n, bars):
    if i == 0:  # Ensure that quick_sort_helper is only called once
        quick_sort_helper(arr, 0, n - 1, bars)


if __name__ == "__main__":
    sort_functions = {
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "selection_sort": selection_sort,
        "quick_sort": quick_sort
    }

    print("Available sorting algorithms:")
    for i, key in enumerate(sort_functions.keys()):
        print(f"{i + 1}. {key}")

    choice = int(input("Enter the number corresponding to the sorting algorithm you want to visualize: "))
    sort_func = list(sort_functions.values())[choice - 1]

    size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for _ in range(size)]

    visualize_sort(sort_func, arr)
