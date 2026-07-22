class Solution:
    def isValid(self, s: str) -> bool:
        string = []
        dic = {")":"(","]":"[", "}":"{"}
        for c in s:
            if c in dic:
                if string and string[-1] == dic[c]:
                    string.pop()
                else:
                    return False
            else:
                string.append(c)
        return True if not string else False