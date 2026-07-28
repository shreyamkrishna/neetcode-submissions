# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        if n <= 1:
            return pairs

        m = n //2
        L = self.mergeSort(pairs[0:m])
        R = self.mergeSort(pairs[m:])

        l, r, arr = 0, 0, 0

        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                pairs[arr] = L[l]
                l += 1
            else:
                pairs[arr] = R[r]
                r += 1
            arr += 1
        
        while l < len(L):
            pairs[arr] = L[l]
            l += 1
            arr +=1
        while r < len(R):
            pairs[arr] = R[r]
            r += 1
            arr += 1
        return pairs