class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}

        for num in nums:
            if num in numbers:
                numbers[num] = numbers[num] + 1
            else:
                numbers[num] = 1
        
        for num in numbers:
            if numbers[num] > 1:
                return True
        return False

        