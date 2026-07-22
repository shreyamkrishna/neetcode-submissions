class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stringStack = []
        dictionary={"}":"{","]":"[",")":"("}

        for char in s:
            print (char, stringStack)
            if char in dictionary.keys():
                if stringStack and dictionary[char]==stringStack[-1]:
                    stringStack.pop()
                else:
                    return False
            else:
                stringStack.append(char)
        
        return True if not stringStack else False
