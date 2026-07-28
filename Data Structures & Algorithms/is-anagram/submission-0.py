class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for char in s:
            if char in dic1.keys():
                dic1[char]+=1
            else:
                dic1[char] = 1

        for char in t:
            if char in dic2.keys():
                dic2[char]+=1
            else:
                dic2[char] = 1

        return dic1 == dic2