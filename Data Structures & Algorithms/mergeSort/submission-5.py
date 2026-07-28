# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelperFn(pairs,0,len(pairs)-1)
    
    def mergeSortHelperFn(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        
        m = ( e + s )//2

        self.mergeSortHelperFn(pairs, s, m)
        self.mergeSortHelperFn(pairs, m+1, e)

        self.merge(pairs,s,m,e)

        return pairs

    def merge(self, pairs, s, m, e):

        L = pairs[s:m+1]
        R = pairs[m+1:e+1]

        Lptr =0
        Rptr = 0
        ArrPtr = s

        while Lptr < len(L) and Rptr < len(R):
            
            if L[Lptr].key <= R[Rptr].key:
                pairs[ArrPtr] = L[Lptr]
                Lptr += 1
            else:
                pairs[ArrPtr] = R[Rptr]
                Rptr += 1
            
            ArrPtr += 1
        
        while Lptr < len(L):
            pairs[ArrPtr] = L[Lptr]
            Lptr += 1
            ArrPtr += 1
        
        while Rptr < len(R):
            pairs[ArrPtr] = R[Rptr]
            Rptr += 1
            ArrPtr += 1
        
        return pairs