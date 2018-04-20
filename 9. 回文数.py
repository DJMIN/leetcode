class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            newx = x
        else:
            return False

        res = 0

        while newx != 0:
            res *= 10
            res += newx % 10
            newx //= 10

        return res == x
