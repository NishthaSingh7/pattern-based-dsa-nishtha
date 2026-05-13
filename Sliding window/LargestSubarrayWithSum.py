# Problem: Largest Subarray With Given Sum
# Pattern: Sliding Window
# Type: Variable Size Window
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: Works only for positive integers

def largest_subarray_with_sum(arr, target_sum):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        # Shrink window if current sum exceeds target
        while current_sum > target_sum:
            current_sum -= arr[left]
            left += 1

        # Update maximum length if target sum is found
        if current_sum == target_sum:
            max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    arr = [3, 2, 4, 5, 1, 1, 1, 1, 1, 3, 3]
    target_sum = 5

    result = largest_subarray_with_sum(arr, target_sum)

    print(f"Maximum subarray length: {result}")