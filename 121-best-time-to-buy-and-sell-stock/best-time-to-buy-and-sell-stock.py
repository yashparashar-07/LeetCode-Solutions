class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        n=len(prices)
        min_price=float('inf')
        for i in range(0,n):
                min_price=min(min_price,prices[i])
                max_profit=max(max_profit,prices[i]-min_price)
        return max_profit
     
     

prices=[7,1,5,3,6,4]
obj=Solution()
obj.maxProfit(prices)
               
       
        