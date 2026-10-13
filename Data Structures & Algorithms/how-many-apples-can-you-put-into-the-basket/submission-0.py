class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight = sorted(weight)
        apples = curr = 0
        
        for w in weight:
            curr += w

            if curr>5000:
                break
            apples += 1
        
        return apples
        