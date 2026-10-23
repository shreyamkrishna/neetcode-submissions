class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        maxWeight = 5000
        weight.sort()
        count = 0
        for w in weight:
            maxWeight -= w
            if maxWeight < 0:
                break
            count += 1
        return count