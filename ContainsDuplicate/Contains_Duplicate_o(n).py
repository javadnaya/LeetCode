class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
    
    
sol= Solution()
  
print(sol.containsDuplicate([1,2,3,4,3])) 