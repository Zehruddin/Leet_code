class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:
            return True
        if x>0:
            temp=x
            sum=0
            while x>0:
                num=x%10
                sum=sum*10+num
                x//=10
            if sum==temp:
                return True
            else:
                return False
        else:
            return False
