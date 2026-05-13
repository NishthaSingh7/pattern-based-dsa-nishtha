# Problem: Largest Subarray With Given Sum
# Pattern: Prefix Sum + HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Works for positive, negative, and zero values

def largest_subarray_with_sum_mixed(arr, target_sum):
    prefix_sum = 0
    prefix_sum_map = {}
    max_length = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Case 1:
        # Subarray from index 0 to i has target sum
        if prefix_sum == target_sum:
            max_length = i + 1

        # Case 2:
        # Check if (prefix_sum - target_sum) exists
        remaining = prefix_sum - target_sum

        if remaining in prefix_sum_map:
            length = i - prefix_sum_map[remaining]
            max_length = max(max_length, length)

        # Store prefix sum only if seen first time
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i

    return max_length


if __name__ == "__main__":
    arr = [-3, 2, 4, 5, 1, 1, 1, -1, 1, 3, 3]
    target_sum = 5

    result = largest_subarray_with_sum_mixed(arr, target_sum)

    print(f"Maximum subarray length: {result}")