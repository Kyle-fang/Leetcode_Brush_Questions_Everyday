class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #对列表进行排序
        #print(nums)
        N = len(nums)
        flag = False
        for x in range(N-1):
            if nums[x] == nums[x+1]:
                flag = True
                break
        return flag

            
