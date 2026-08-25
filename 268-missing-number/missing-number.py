class Solution(object):
    def missingNumber(self, nums):
       n=len(nums)
       for i in range(0,n+1):
        if i not in nums:
            return i


obj=Solution()
nums=[3,0,1]
obj.missingNumber(nums)
    
        