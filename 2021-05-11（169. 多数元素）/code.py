class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() #对数组排序
        #print(nums)
        return nums[len(nums)//2]
