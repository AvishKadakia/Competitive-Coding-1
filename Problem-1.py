
# Find the Missing Number in a sorted array
'''
Solution:
    missingNumber(self, nums):
        n is length of nums
        Space Complexity: O(1)
        Time Complexity: O(log n)
'''
class Solution:
    def missingNumber(self, nums)
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            mid = l +(( r - l) // 2)
            if mid != nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        if l == len(nums) - 1 and nums[l] != l:
            l -= 1
        return  min(l + 1,r+1)
