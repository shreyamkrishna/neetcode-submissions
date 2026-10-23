class Solution:
    def countLetters(self, s: str) -> int:
        consLetters = 1
        total = 0 
        if len(s) > 1:
            for i in range(1, len(s)):
                print( i , s[i], consLetters)
                if s[i]==s[i-1]:
                    consLetters+= 1
                else:
                    total += (consLetters * (consLetters + 1)//2)
                    consLetters = 1
                    print("Total", total)
            total += (consLetters * (consLetters + 1)//2)
            return total 
        else:
            return 1        
        