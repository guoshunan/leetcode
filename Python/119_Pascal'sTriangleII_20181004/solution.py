class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            result=[]
            pre_row = self.getRow(rowIndex-1)
            for i in range(0,len(pre_row)-1):
                result.append(pre_row[i]+pre_row[i+1])
            return [1]+result+[1]