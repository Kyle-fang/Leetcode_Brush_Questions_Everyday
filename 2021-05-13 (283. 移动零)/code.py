class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        n = 0
        for x in range(N):
            if nums[x] == 0:
                #nums.append(0)
                n = n + 1
        for y in range(n):
            nums.remove(0)
            nums.append(0)
