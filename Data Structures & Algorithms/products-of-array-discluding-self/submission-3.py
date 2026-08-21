class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. Prefix products: multiply elements to the left
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # 2. Suffix products: multiply elements to the right
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res