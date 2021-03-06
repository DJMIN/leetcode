class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            res = x % 10
            while x >= 10:
                x //= 10
                res *= 10
                res += x % 10
            if res > 2147483648:
                return 0
        else:
            x = -x
            res = x % 10
            while x >= 10:
                x //= 10
                res *= 10
                res += x % 10
            if res > 2147483648:
                return 0
            res = -res

        return res
