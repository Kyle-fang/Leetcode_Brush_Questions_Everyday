  class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        index = 0
        for x in range(N):
            if nums[x] != val:
                nums[index] = nums[x]
                index += 1
        del nums[index:N]
        return len(nums)
