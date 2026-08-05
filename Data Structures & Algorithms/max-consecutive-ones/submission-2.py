class Solution:
    def findMaxConsecutiveOnes(self, nums):
        highest = {}
        count = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
                highest[i] = count
            elif num == 0:
                count = 0
                highest[i] = count
        return max(highest.values())