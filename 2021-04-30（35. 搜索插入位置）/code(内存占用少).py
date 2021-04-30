class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        Find = 0   #是否找到标志位
        for x in range(N):
            if nums[x] == target:
                return x
                Find = 1       #找到目标值
        #if Find == 0:
        if target > nums[N-1]:
            return N
        elif nums[0] > target:
            return 0
        else:
            for y in range(N-1):
                if nums[y] < target < nums[y+1]:
                    return y+1
            
             
