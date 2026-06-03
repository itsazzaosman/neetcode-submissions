class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_val = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_val = max(current_count, max_val) 
            else:
                current_count = 0
        return max_val