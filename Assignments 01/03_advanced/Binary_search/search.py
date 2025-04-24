def binary_search(arr, target):
    """
    Perform binary search to find the target value in a sorted list.

    Parameters:
    arr (list): The sorted list to search within.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    # Set the initial left and right pointers
    left = 0
    right = len(arr) - 1

    # Loop until the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the target is at the middle index
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half, move the left pointer
        else:
            right = mid - 1  # Target is in the left half, move the right pointer

    return -1  # If we exit the loop, the target was not found

def main():
    # Get the input list from the user (must be sorted)
    arr = list(map(int, input("Enter a sorted list of numbers (separated by spaces): ").split()))
    
    # Get the target value to search for
    target = int(input("Enter the target value: "))
    
    # Call the binary search function
    result = binary_search(arr, target)
    
    # Print the result
    if result != -1:
        print(f"Target found at index {result}.")
    else:
        print("Target not found in the list.")

if __name__ == "__main__":
    main()
