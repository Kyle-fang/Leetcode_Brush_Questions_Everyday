class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        for x in range(len(nums)):
            for y in range(len(nums)):
            #print(nums[x],nums[y])
                if x != y:
                    #print(8,x,y)
                    if nums[x] + nums[y] == target:
                        #print(9,x,y)
                        list = [x,y]
                        return list
            #print(len(list))
            if len(list) > 1:
                break
