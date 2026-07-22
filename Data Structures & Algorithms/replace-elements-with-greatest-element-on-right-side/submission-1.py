class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        for i in range(l):
            if i == l-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
        return arr