"""
Module for implementing the Merge Sort algorithm.
"""

def mergesort(lst):
    """
    Sorts a list in ascending order using the merge sort algorithm.
    
    Args:
        lst (list): The list to be sorted.
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Recursively sort both halves
        mergesort(left_half)
        mergesort(right_half)

        # Merge sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    lst = [5, 5, 2, 4, 1, 6]
    print("Original List:", lst)
    mergesort(lst)
    print("Sorted List:", lst)
