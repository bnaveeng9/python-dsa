from typing import List
import math


def merge_sort(unsorted_list: List[int]) -> None:
    """
    Sort a list of integers in ascending order using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer sorting algorithm that recursively
    divides the input list into smaller sublists until each sublist contains
    a single element. The sublists are then merged back together in sorted
    order.

    Args:
        unsorted_list (List[int]):
            The list of integers to be sorted.

    Returns:
        None:
            The input list is sorted in place.

    Example:
        >>> numbers = [5, 2, 8, 1, 3]
        >>> merge_sort(numbers)
        >>> print(numbers)
        [1, 2, 3, 5, 8]

    Time Complexity:
        O(n log n)

    Space Complexity:
        O(n)
    """
    if len(unsorted_list) > 1:

        # Calculate the midpoint of the list.
        mid = math.floor(len(unsorted_list) / 2)

        # Split the list into left and right halves.
        leftarr = unsorted_list[:mid]
        rightarr = unsorted_list[mid:]

        # Recursively sort both halves.
        merge_sort(leftarr)
        merge_sort(rightarr)

        # Initialize pointers for left array, right array,
        # and merged array.
        i, j, k = 0, 0, 0

        # Merge the two sorted halves into the original list.
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] <= rightarr[j]:
                unsorted_list[k] = leftarr[i]
                i += 1
            else:
                unsorted_list[k] = rightarr[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left half.
        while i < len(leftarr):
            unsorted_list[k] = leftarr[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right half.
        while j < len(rightarr):
            unsorted_list[k] = rightarr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    """
    Demonstrates the Merge Sort algorithm using a sample list.
    """
    arr: List[int] = [1, 5, 3, 4, 2, 6]

    print("Original list:", arr)

    merge_sort(arr)

    print("Sorted list:", arr)