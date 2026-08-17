class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right = len(arr) - 1
        left = 0
        max_element = 0
        while left < right:
            if arr[right] > max_element:
                max_element = arr[right]
    
            if right == left + 1:
                arr[left] = max_element
                max_element = 0
                left += 1
                right = len(arr) - 1
            else:
                right -= 1
            
        arr[-1] = -1
        return arr

        