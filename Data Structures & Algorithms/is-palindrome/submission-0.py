class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start<end:
            if s[start].isalnum(): 
                print("start", s[start])
                if s[end].isalnum():
                    print("end", s[end])
                    if (s[start].lower()==s[end].lower()):
                        start += 1
                        end -= 1
                    else:
                        return False
                else:
                    end -=1
            else:
                start += 1
            
        return True