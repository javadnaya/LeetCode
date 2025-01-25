class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
 
        numbers_set = set(nums)
        
        res = []
        for num in range(1,len(nums)+1):
            if num not in numbers_set:
                res.append(num)
        return res
 