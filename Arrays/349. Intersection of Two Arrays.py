# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.


from Arrays import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = [0] * 1001
        ans = [0] * 1001
        j = 0

        for a in nums1:
            freq[a] = -1

        for a in nums2:
            if freq[a] == -1:
                ans[j] = a
                j += 1
                freq[a] = 1

        res = [0] * j
        for i in range(j):
            res[i] = ans[i]

        return res