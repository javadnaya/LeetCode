class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
 
        numbers = list(range(1,len(nums)+1))
        
        res = []
        for num in numbers:
            if num not in nums:
                res.append(num)
        return res
    
sol = Solution()
print(sol.findDisappearedNumbers([1,1]))        