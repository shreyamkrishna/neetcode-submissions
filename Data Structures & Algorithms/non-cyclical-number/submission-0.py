class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            num = str(n)
            numSum = 0
            for i in range(len(num)):
                numSum += int(num[i])**2
            
            return numSum

        
        seen = set()

        while n not in seen:
            seen.add(n)
            n = helper(n)
            if n ==1:
                return True
        
        return False