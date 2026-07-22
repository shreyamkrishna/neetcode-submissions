class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for i in range(length):
            if (i == (length-1)):
                arr[i]= -1
            else:
                arr[i] = max(arr[i+1:])
            
        return arr