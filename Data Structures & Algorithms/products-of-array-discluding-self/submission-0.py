class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        op = []
        prefix = []
        suffix= []

        product = 1
        for num in nums:
            product *= num
            prefix.append(product)

        product = 1
        for num in nums[::-1]:
            product *= num
            suffix.append(product)
        suffix = suffix[::-1]
        for i in range(len(nums)):
            left = prefix [i-1] if i >0 else 1
            right = suffix [i+1] if i<(len(nums)-1) else 1
            op.append(left * right)
        
        return op