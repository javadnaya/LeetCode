class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        num_set = set(nums) 
        n = len(nums)
        
        for i in range(1, n + 1):
            if i not in num_set:  
                return i


sol = Solution()
print(sol.missingNumber([0,1,3]))