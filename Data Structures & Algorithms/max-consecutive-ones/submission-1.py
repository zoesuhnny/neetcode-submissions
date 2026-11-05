class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c = 0
        count=0
        for i in range(len(nums)):
            #1010 -> would be 1
            #110111: 1, then 2, remains 2, then remains 2 but start counting, then 3>2.

            if nums[i]==1:
                count=count+1
            else:
                if count > max_c: max_c = count
                count = 0
            
            if count > max_c: max_c = count

        return max_c
            #each iteration/i = checking each number

                    

        