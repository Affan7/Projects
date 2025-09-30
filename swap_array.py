def sawp(nums):
    left, right = 0, len(nums)-1
    while (left<right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right]= temp
        left += 1
        right -= 1
    return nums
nums = [1,2,3,4,5]
print((sawp(nums)))

