class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valCounter = 0
        for i in range(len(nums)):
            if nums[i]==val: 
                valCounter += 1
            else:
                nums[i-valCounter] = nums[i]
            
        return len(nums) - valCounter