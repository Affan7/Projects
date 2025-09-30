#2) Maximum Sum Subarray (also return indices)
#Prompt: Return both the max sum and the (start, end) indices of a subarray achieving it.
#Hint: Track a temp_start that resets when you restart at x. Update (start, end) whenever best improves.
#Time/Space: O(n) / O(1)
def max_subarray_sum_with_indices(nums):
    if not nums:
        raise ValueError("nums must be non-empty")

    curr = 0
    best = float('-inf')
    left = right = temp_left = 0

    for i, num in enumerate(nums):
        if num > curr + num:      # restart if past hurts
            curr = num
            print(curr)
            temp_left = i
            print(temp_left)
        else:                      # extend
            curr += num
            print(curr)

        if curr > best:            # record best (even if negative)
            best = curr
            print(best)
            left, right = temp_left, i
            print(right)

    return best, (left, right)

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best_sum, (start, end) = max_subarray_sum_with_indices(nums)
print(f"Best sum: {best_sum}")
print(f"Start index: {start}, End index: {end}")
print(f"Subarray: {nums[start:end+1]}")

