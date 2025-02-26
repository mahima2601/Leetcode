class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        i=0
        n=len(s)
        for j in range(len(t)):
            if s[i]==t[j]:
                i+=1
            if i>n-1:
                return True
        if i<=n-1:
            return False

        
        
        

            
        