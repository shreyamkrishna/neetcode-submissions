class Solution:
    def isValid(self, s: str) -> bool:
       
       dictionary = {"}":"{", "]":"[", ")":"("}
       string=[]
       for i in s:
            if i in dictionary.keys():
                if string and dictionary[i]==string[-1]:
                    string.pop()
                    print(string)
                else:
                    return False
                
            else:
                string.append(i)
                print (string)
       return True if not string else False