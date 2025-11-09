"""
The Art of Approximation 
Difficulty: Medium

Question: Binary search is effective, since we all know that its time complexity is O(logn). But in large scale systems like Netflix, where there are trillions of megabytes to process, even this may fall short. In large scale systems like that of Netflix, data lookups are always parallel, simultaneously searching relevant node servers in a server cluster. The data at Netflix is stored redundantly in such a way that they can be accessed in the fastest way possible. So to compensate for this, one of the approaches they apply is to approximate search solutions inside their massive data store. A way to start that is to use Approximate Binary Search. This basically means that after a certain number of calls to itself, the binary search either returns the result or a value that says “Not found here”. As a developer, your task is to devise the algorithm. Assume that the data you are getting is sorted, but you don't know which direction. Thus, given an upper limit on the number of self-calls you can make, write a program that searches the data and returns either the index of where the data is, or -1 (indicating that the data is nowhere to be found within the given constraints.) Your task is to complete the function:

def approximate_binary_search(data, search_term, limit) 
    Input Format:
    •    data - list of int
    •    search_term: int
    •    limit: int
Output Format: int

Examples:
Test Case 1:
Input: [1, 2, 3, 4, 5, 6], 1, 2
Output: -1
Explanation: Initially, the middle element is checked. Since 1 isn't in the middle, there are 2 recursive calls - one to the left half, and one to the right. The left half gets the array [1, 2, 3], while the right half gets [4, 5, 6]. Now, each of their middle elements are 2 and 5 respectively. Now, they are going to be split again, but due to the constraint that the maximum number of API calls can be 2, it returns -1. NB: Assume that the limit is going to be an even number.
"""


def approximate_binary_search(data: list[int], search_term: int, limit: int) -> int:
    """
    Perform an approximate binary search on a sorted list of integers within a certain number of steps.

    Args:
        data: Sorted list of integers (ascending or descending)
        search_term: The integer to search for
        limit: The maximum number of calls allowed (an even number)
    Returns:
        int: The index of the search_term in data if found, otherwise -1
    """
    assert limit % 2 == 0
    l, r = 0, len(data) - 1
    asc = data[l] < data[r]

    while l <= r and limit > 0:
        mid = (l + r) // 2
        if data[mid] == search_term:
            return mid
        if asc:
            if data[mid] < search_term:
                l = mid
            else:
                r = mid
        else:
            if data[mid] < search_term:
                r = mid
            else:
                l = mid
        limit -= 1

    return -1


def test_1():
    assert approximate_binary_search([1, 2, 3, 4, 5, 6], 1, 2) == -1


def test_2():
    assert approximate_binary_search([1, 2, 3, 4, 5, 6], 1, 4) == 0


if __name__ == "__main__":
    test_1()
    test_2()
    # ?? honestly, didn't quite understand this problem and saw no followup
    # TODO leaving tests for whenever this is clarified
    print("All tests passed.")
