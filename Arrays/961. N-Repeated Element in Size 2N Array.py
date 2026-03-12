# You are given an integer array nums with the following properties:
# 1.nums.length == 2 * n.
# 2.nums contains n + 1 unique values, n of which occur exactly once in the array.
# 3.Exactly one element of nums is repeated n times.
# 4.Return the element that is repeated n times.

from Arrays import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)