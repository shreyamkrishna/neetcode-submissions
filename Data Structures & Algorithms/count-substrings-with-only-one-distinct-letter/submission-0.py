class Solution:
    def countLetters(self, s: str) -> int:
        l = total = 0
        
        for r in range(len(s) + 1):
            if r== len(s) or (s[l] != s[r]):
                substringLen = r - l

                total += substringLen * (substringLen +1 ) // 2 

                l = r
        return total 