"""
Manual Work
Difficulty: Medium
What will the following list look like after 2 iterations of bubble sort?

[5, 7, 11, 2, 4]

Note - Move from the beginning to end of the list 2 times.

Options:
- [5, 7, 4, 2, 11]
- [5, 4, 2, 7, 11]
X [5, 2, 4, 7, 11]
- [2, 4, 5, 7, 11]

After each iteration, the largest unsorted element will find its correct place. Thus, after 2 iterations, the 2 largest elements will be in their correct places, and the rest of elements will be in the same order.

Iteration 1: [5, 7, 2, 4, 11]
Iteration 2: [5, 2, 4, 7, 11]
"""


def bubble_sort(arr, num_iters):
    """
    Modified bubble sort that terminates after a certain number of iterations.

    Args:
        arr (list): The list to be sorted
        num_iters (int): The number of iterations to perform
    Returns:
        list: The partially sorted list after the specified number of iterations
    """
    n = len(arr)

    for i in range(num_iters):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr


def test():
    assert bubble_sort([5, 7, 11, 2, 4], 2) == [5, 2, 4, 7, 11]


if __name__ == "__main__":
    test()
    print("All tests passed.")
