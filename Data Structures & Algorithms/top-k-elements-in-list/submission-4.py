class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1

        op = []
        for i in range(k):
            maxfreq = 0
            maxkey = -1
            for key in dic.keys():
                if dic[key] > maxfreq:
                    maxfreq = dic[key]
                    maxkey = key
            op.append(maxkey)
            del dic[maxkey]

        return op