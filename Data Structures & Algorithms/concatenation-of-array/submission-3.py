class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nl = 2*l 
        ans=[0]* nl
        ans[:l] = nums
        ans[l:] = nums
        return ans
