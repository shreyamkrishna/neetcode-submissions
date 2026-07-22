class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len (nums)
        maxOnes = 0
        ones = 0
        for i in range(length):
            if (nums[i]==1):
                ones += 1
            else:
                maxOnes = max(ones, maxOnes)
                ones = 0
        maxOnes = max(ones, maxOnes)
        return maxOnes