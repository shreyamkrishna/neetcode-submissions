class Solution:
    def isValid(self, s: str) -> bool:
        dic ={"]":"[", "}":"{",")":"("}
        stack=[]
        # ()
        for c in s:
            if c in dic.keys():
                if stack and dic[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False