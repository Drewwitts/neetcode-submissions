class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        capacity = len(nums) * 2
        ans = [0] * capacity
        for i in range(len(nums)):
            ans[i] = nums[i]
        
        index = len(nums)
        for i in range(len(nums)):
            ans[index] = nums[i]
            index+=1
        return ans

        
