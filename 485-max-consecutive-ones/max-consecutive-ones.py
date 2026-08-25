class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_count=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]==1:
                count+=1
            else:
                max_count=max(count,max_count)
                count=0

        max_count=max(count,max_count)#for the last edge case  
        return max_count
        
nums=[1,1,0,1,1,1]
obj=Solution()
obj.findMaxConsecutiveOnes(nums)