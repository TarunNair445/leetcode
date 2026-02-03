class Solution(object):
    def isSubsequence(self, s, t):
        n = len(s)
        count = 0 
        j = 0
        for i in range(len(s)):
            for k in range(j,len(t)):
                if(s[i]==t[k]):
                    j = k+1
                    count = count +1
                    break
        
        if(count >= n):
            return True
        else:
            return False


        