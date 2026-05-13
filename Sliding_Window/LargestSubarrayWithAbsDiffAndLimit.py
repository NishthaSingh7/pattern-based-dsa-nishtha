# Problem: Longest Continuous Subarray With Absolute Difference Less Than or Equal to Limit
# Pattern: Sliding Window + Monotonic Queue
# Type: Variable Size Window
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note:
# - maxQ stores elements in decreasing order
# - minQ stores elements in increasing order
# - Helps track maximum and minimum values in current window efficiently

from collections import deque


def longest_subarray_with_limit(nums, limit):
    max_queue = deque()
    min_queue = deque()

    left = 0
    max_length = 0

    for right in range(len(nums)):

        # Maintain decreasing queue for maximum values
        while max_queue and nums[max_queue[-1]] < nums[right]:
            max_queue.pop()

        max_queue.append(right)

        # Maintain increasing queue for minimum values
        while min_queue and nums[min_queue[-1]] > nums[right]:
            min_queue.pop()

        min_queue.append(right)

        # Shrink window if absolute difference exceeds limit
        while nums[max_queue[0]] - nums[min_queue[0]] > limit:

            # Remove indices outside current window
            if max_queue[0] == left:
                max_queue.popleft()

            if min_queue[0] == left:
                min_queue.popleft()

            left += 1

        # Update maximum valid window length
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":

    nums = [8, 2, 4, 7]
    limit = 4

    result = longest_subarray_with_limit(nums, limit)

    print(f"Longest valid subarray length: {result}")