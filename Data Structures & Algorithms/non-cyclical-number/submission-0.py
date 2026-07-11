class Solution:
    def getNext(self, n):    
        sum=0
        while(n>0):
            digit=n%10
            sum+=digit*digit
            n//=10
        return sum
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.getNext(n)
        while(slow!=fast):
            slow=self.getNext(slow)
            fast=self.getNext(self.getNext(fast))
        return slow==1        
        