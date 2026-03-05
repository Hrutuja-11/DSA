# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums) -> int:
        curr_sum = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum>max_sum:
                max_sum = curr_sum
            if curr_sum<0:
                curr_sum = 0
            
        return max_sum