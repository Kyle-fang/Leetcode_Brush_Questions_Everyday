class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        '''加1后无需进位'''
        if digits[N-1]+1 < 10:
            digits[N-1] = digits[N-1] + 1
            return digits
        '''加1后需要进位'''
        else:
            digits[N-1] = digits[N-1] + 1   #先加1
            for x in range(N):
                digits[N-1] = digits[N-1] - 10
                #print(digits)
                #print(digits[N-2])
                if digits[N-2] <= 0:
                    digits.insert(0, 1)
                    #print(digits[N-2])
                else:
                    digits[N-2] = digits[N-2] + 1
                if digits[N-2] < 10:
                    break
                N = N -1
            return digits
