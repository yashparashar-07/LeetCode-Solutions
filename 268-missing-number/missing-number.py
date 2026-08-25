class Solution(object):
        def missingNumber(self, nums):
            n=len(nums)
            calsum=(n*(n+1))//2
            actualsum=sum(nums)
            return calsum-actualsum


obj=Solution()
nums=[3,0,1]
obj.missingNumber(nums)
        
            