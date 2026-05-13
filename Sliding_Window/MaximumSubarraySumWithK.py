# Problem: Maximum Sum Subarray of Size K
# Pattern: Sliding Window
# Type: Fixed Size Window
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_subarray_sum(arr, k):
    left = 0
    current_sum = 0
    max_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        # Maintain fixed window size
        if (right - left + 1) > k:
            current_sum -= arr[left]
            left += 1

        # Update max sum when window size becomes k
        if (right - left + 1) == k:
            max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    arr = [100, 200, 150, 300, 20, 50, 200]
    k = 2

    result = max_subarray_sum(arr, k)

    print(f"Maximum subarray sum of size {k}: {result}")