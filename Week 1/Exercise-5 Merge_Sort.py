# Function to perform Merge Sort
def merge_sort(arr):

    # Check if the array has more than one element
    if len(arr) > 1:

        # Find the middle index
        mid = len(arr) // 2

        # Divide the array into left half
        left = arr[:mid]

        # Divide the array into right half
        right = arr[mid:]

        # Recursively sort the left half
        merge_sort(left)

        # Recursively sort the right half
        merge_sort(right)

        # Initialize pointers
        i = j = k = 0

        # Merge the two sorted halves
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # Copy remaining elements from left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Input array
numbers = [38, 27, 43, 3, 9, 82, 10]

print("Before Sorting:")
print(numbers)

# Call Merge Sort
merge_sort(numbers)

print("After Sorting:")
print(numbers)