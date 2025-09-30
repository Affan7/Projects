from collections import Counter
def largestElement(nums):
    f = Counter(nums)
    return f
nums = [1, 1, 2, 2,3,3]
print(largestElement(nums))
