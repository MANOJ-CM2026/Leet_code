class Solution:
    def smallestBalancedIndex(self, nums):
        navorelitu = nums
        
        n = len(nums)
        
        # compute right products
        right = [1] * n
        prod = 1
        
        for i in range(n - 1, -1, -1):
            right[i] = prod
            prod *= nums[i]
            if prod > 10**15:   # limit to avoid huge numbers
                prod = 10**15
        
        left_sum = 0
        
        for i in range(n):
            if left_sum == right[i]:
                return i
            left_sum += nums[i]
        
        return -1