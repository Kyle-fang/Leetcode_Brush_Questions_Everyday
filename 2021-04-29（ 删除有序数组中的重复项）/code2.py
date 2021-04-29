class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''双指针思想'''
        L = 0
        for R in range(1,len(nums)):
            if nums[L] != nums[R]:
                L = L + 1
                nums[L] = nums[R]
        return L + 1
