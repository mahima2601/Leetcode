class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            else:
                seen.add(n)
           
            square=[]
            for i in str(n):
                digit_square=int(i)**2
                square.append(digit_square)
            n=sum(square)
        return True

        