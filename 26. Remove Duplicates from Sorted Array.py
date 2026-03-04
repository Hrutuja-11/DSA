# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.


class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        start = 0
        for i in range(1,n):
            if nums[i] != nums[start]:
                start+=1
                nums[start] = nums[i]
        return start+1