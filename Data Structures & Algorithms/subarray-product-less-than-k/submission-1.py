class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        length, res = len(nums), 0
        curProd = 1
        left = 0

        for j in range(length):
            curProd *= nums[j]
            while curProd >= k:
                curProd //= nums[left]
                left += 1
            res += j - left + 1

        return res