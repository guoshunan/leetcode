class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus_one = int("".join([str(x) for x in digits]))+1
        return [int(x) for x in list(str(plus_one))]