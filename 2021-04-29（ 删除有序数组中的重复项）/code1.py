class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list = []
        J = 0  #标志位，该元素后边是否有相同的元素
        #print("a", list)
        for x in range(len(nums)-1):
            J = 0
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    J = 1
            if J == 0:
                list.append(nums[x])
        list.append(nums[len(nums)-1])
        nums = list
        #print(list)
        return len(nums)
