class Solution:
    def toHexspeak(self, num: str) -> str:
        hexNum = str(hex(int(num))).upper()[2:]

        hexNum = hexNum.replace("0","O")
        hexNum = hexNum.replace("1","I")
    
        if all( c in "ABCDEFIO" for c in hexNum):
            return hexNum
        else:
            return "ERROR"
        
        
