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

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            strx = str(x)
            le = len(strx)
            le1 = le - 1
            halfle = le // 2
            for index, ch in enumerate(strx):
                print(ch , strx[le1-index])
                if ch != strx[le1-index]:
                    return False
                if index > halfle:
                    break
            return True
        else:
            return False



print(Solution().isPalindrome(121))

