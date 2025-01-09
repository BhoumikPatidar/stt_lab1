"""
Module for implementing the Merge Sort algorithm.
"""

def mergesort(array):
    """
    Sorts a list in ascending order using the merge sort algorithm.
    Args:
        array (list): The list to be sorted.
    """
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        # Recursively sort both halves
        mergesort(left_half)
        mergesort(right_half)

        # Merge sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    # Define the list to be sorted
    input_list = [5, 5, 2, 4, 1, 6]
    print("Original List:", input_list)
    # Call the mergesort function
    mergesort(input_list)
    print("Sorted List:", input_list)
