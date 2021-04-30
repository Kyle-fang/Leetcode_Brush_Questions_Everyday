class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        max = -10**5
        for x in range(N):
            M = 0
            for y in range(x, N):
                M = M + nums[y]
                if M >= max:
                    max = M
        return max
