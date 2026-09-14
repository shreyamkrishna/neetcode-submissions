class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newStrs = ["".join(sorted(i)) for i in strs]
        dictionary = {}
        strNo = 0
        for i,s in enumerate(newStrs):
            if s not in dictionary:
                dictionary[s]= []
                dictionary[s].append(strs[i])
            else:
                dictionary[s].append(strs[i])
        op  =[]
        for key in dictionary.keys():
            op.append(dictionary[key])
        
        return op