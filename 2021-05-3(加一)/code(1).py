class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        num = 0
        for x in range(N):
            num = num + digits[x]*(10**(N-1))
            N = N - 1
        num = num + 1
        print(num)
        L = len(str(num))
        nums = []
        for y in range(L):
            X = num % 10
            nums.insert(0,X)
            num = int(num/10)     #取整后，失真
        return nums
