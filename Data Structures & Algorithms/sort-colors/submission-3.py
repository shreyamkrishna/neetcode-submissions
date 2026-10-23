class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        clrs = [0] * 3
        for n in nums:
            clrs[n] += 1

        i = 0
        for n in range(len(clrs)):
            for _ in range(clrs[n]):
                nums[i] = n
                i += 1
        
        return nums