class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  
        for _ in range(k):
            last = nums[-1]
            for j in range(n-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = last