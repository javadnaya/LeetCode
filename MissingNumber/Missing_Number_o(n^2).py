class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        numbers = list(range(1,len(nums)+1))

        for i in numbers:
            if i  not in nums:
                return i
            
            
sol = Solution()
print(sol.missingNumber([0,1,3]))
            