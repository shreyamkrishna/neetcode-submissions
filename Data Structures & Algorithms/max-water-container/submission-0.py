class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        maxWaterAmt = 0
        while l < r:
            waterAmt = (r - l)* min(heights[l], heights[r])
            maxWaterAmt = max(maxWaterAmt, waterAmt)
            if heights[l] <= heights[r]: 
                l += 1
            else:
                r-=1
        
        return maxWaterAmt