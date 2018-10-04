class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x=str(x)
        if str_x[0].isnumeric():
            reverse_str_x=str_x[::-1]
            result = int(reverse_str_x)
        else:
            reverse_str_x=str_x[1:][::-1]
            result = int(str_x[0]+reverse_str_x)
        if abs(result) > 2 ** 31 - 1:
            return 0
        else:
            return result