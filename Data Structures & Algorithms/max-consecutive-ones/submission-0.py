class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        empt_list = []
        runner = 0
        for num in nums:
            if num == 1:
                runner +=1
            else:
                empt_list.append(runner)
                runner = 0
        empt_list.append(runner)        
        return max(empt_list)

        