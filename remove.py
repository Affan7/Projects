def removeElement(nums):
        val = 3
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
nums = [2,2,3,4,5,6,6,7]
print(removeElement(nums))

