class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<2:
            list = [[1]]
        else:
            list = [[1], [1, 1]]
            for x in range(numRows-2):
                N = [1, 1]
                L = list[-1]
                #print(L)
                for y in range(len(L)-1):
                    num = L[y] + L[y+1]
                    N.insert(-1, num)
                    #print(N)
                list.append(N)
                #print(list)
        return list
