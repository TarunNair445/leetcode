class Solution(object):
    def zeroFilledSubarray(self, nums):
        one = 0
        total = 0
        for i in range(len(nums)):
            if(nums[i]==0):
                one = one +1
                total = total + one 
            else:
                one = 0
        
        return total

        