class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       n = len(nums)

       ans = [0]*(2*n)

       for i in range(n):
        ans[i+n] = (nums[i])
        ans[i] = (nums[i])

        #let n = 5.
        #iterate 0,1,2,3,4
        #ans[0]=nums[0], ans[0+5]=nums[0]
        #have to read nums twice
        #or assign ans[i] & ans[i+n] -> nums[i] in 1 pass, not 2
        
       return ans
    