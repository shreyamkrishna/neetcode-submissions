class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ns = set(nums)
        longest = 0

        for num in ns:
            print (num)
            if (num - 1) not in ns:
                length = 1
                print("length", length)
                while (num + length) in ns:
                    length += 1
                    #print("length", length)
                longest = max(longest, length)
        return longest