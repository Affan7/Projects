def subarray(nums):
    curr = 0
    best = float('-inf')
    left = right = temp_left = 0
    for i, num in enumerate(nums):
        if (num > curr+num):
            curr = num
            temp_left = i
        else:
            curr = curr+num
        if curr>best:
            best = curr
            left, right = temp_left,i
    return (best,(left, right))

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best_sum, (start, end) = subarray(nums)
print(f"Best sum: {best_sum}")
print(f"Start index: {start}, End index: {end}")
print(f"Subarray: {nums[start:end+1]}")

