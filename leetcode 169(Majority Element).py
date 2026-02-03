class Solution(object):
    def majorityElement(self, nums):
        count = 0 
        c = None
        for num in nums:
            if(count == 0 ):
                c = num
                count = count + 1
            elif(c == num):
                count = count + 1
            else:
                count = count -1
        
        return c
        
        