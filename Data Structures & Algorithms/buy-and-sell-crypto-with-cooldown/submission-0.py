class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold=-prices[0]
        sold=0
        rest=0
        for i in prices[1:]:
            prev=sold
            sold=hold+i
            hold=max(hold,rest-i)
            rest=max(rest,prev)
        return max(sold,rest)