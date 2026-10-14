class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        result = arr[:]
        while True:
            changed = False
            prev = result[:]
            for i in range(1, len(arr) - 1):
                if prev[i] < prev[i+1] and prev[i] < prev[i-1]:
                    result[i] += 1
                    changed = True
                elif prev[i] > prev[i+1] and prev[i] > prev[i-1]:
                    result[i] -= 1
                    changed = True
            if not changed: 
                break
        return result