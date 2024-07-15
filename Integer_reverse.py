class Integer_reverse:
    def reverse(self, x: int) -> int:
        if abs(x) >= 10**9:
            return 0
        else:
            temp=abs(x)
            stemp=str(temp)
            sum=0
            if stemp[0]=="0":
                stemp=stemp.replace("o",'')
            temp=int(stemp)
            while(temp>0):
                n=temp%10
                sum=sum*10+n
                temp//=10
            if x<0:
                return -1*sum
            else:
                return sum
