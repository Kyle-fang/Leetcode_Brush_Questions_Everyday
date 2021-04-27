class Solution:
    def reverse(self, y: int) -> int:
        '''初始化变量，列表'''
        y = int(y)
        n = len(str(y))
        sum = 0
        B = 0
        list = []
        '''判断y是正数还是负数还是0。并将输入整数的每一位拆开，依次放入一个列表中'''
        if y > 0:
            B = 1   #为正数，则标志位为1
            for i in range(n):
                X = y % 10
                list.insert(0,X)
                y = int(y/10)
        elif y < 0:
            B = 0   #为负数，则标志位为0
            n = n - 1
            y = -int(y) 
            for i in range(n):
                X = y % 10
                list.insert(0,X)
                y = int(y/10)
        else :
            list = []

        '''输出反转整数sum'''
        if len(list) == 0:
            sum = 0
        else:
            for j in range(n):
                sum = sum + list[j]*(10**(j))
        '''判断反转整数是否要加符号'''
        if B == 0:
            sum = -int(sum)
        elif B == 1:
            sum = int(sum)

        '''判断反转后整数是否超过32位有符号数的范围，超过则sum=0'''
        if -2**31 > sum or sum > 2**31-1:
            sum = 0
        return sum
