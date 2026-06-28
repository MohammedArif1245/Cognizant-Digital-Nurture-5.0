# Function to perform Binary Search
def binary_search(arr, target):

    # Initialize the starting index
    low = 0

    # Initialize the ending index
    high = len(arr) - 1

    # Continue searching until the search space is valid
    while low <= high:

        # Find the middle index
        mid = (low + high) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid

        # If target is smaller, search the left half
        elif target < arr[mid]:
            high = mid - 1

        # If target is larger, search the right half
        else:
            low = mid + 1

    # Return -1 if the target is not found
    return -1


# Sorted array for Binary Search
numbers = [2, 5, 8, 10, 15, 18, 25]

# Element to search
target = 10

# Call the Binary Search function
result = binary_search(numbers, target)

# Check whether the element is found
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")