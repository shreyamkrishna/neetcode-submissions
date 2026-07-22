class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        length = len(nums)
        for i in range(length):
            if (nums[i]==val):
                count += 1
            else: 
                nums[i - count] = nums[i]
        return length - count