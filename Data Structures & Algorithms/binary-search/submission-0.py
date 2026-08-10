class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) -1
        start =0
        
        while end>=start:
            middle = (start+end) //2

            if (nums[middle]>target):
                end = middle - 1
            elif (nums[middle]<target):
                start = middle + 1
            else:
                return middle
        return -1  