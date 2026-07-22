class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = 2 * n
        ans = [0]*t
        ans[:n] = nums
        ans[n:]  = nums
        return ans
