class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        le = len(n)
        halfle = le // 2
        if le == 1:
            return str(int(n) - 1)
        elif le == 2:
            if n == '10' or n == '11':
                return '9'
            elif n == '99':
                return '101'

            temp = int(n[0])
            small = temp * 10 + temp
            if str(small) == n:
                temp -= 1
                return str(temp * 10 + temp)
            temp = int(n[0]) + 1
            big = temp * 10 + temp
            if big - int(n) > int(n) - small:
                return str(small)
            else:
                return str(big)
        elif le == 4:
            if n == '1000':
                return '999'
            small = int(n[:halfle] + n[:halfle][::-1])
            big = int(str(int(n[:halfle]) + 1) + str(int(n[:halfle]) + 1)[::-1])

            if big < 10000:
                if big - int(n) > int(n) - small:
                    return str(small)
                else:
                    return str(big)

        temp = str(int(n[:halfle + 1 if halfle != le / 2 else halfle]) - 1)
        mid = str(int(n[halfle]) - 1) if halfle != le / 2 else ''
        m_small = temp[:-1 if mid else le] + mid + temp[::-1][1 if mid else 0:]
        small = n[:halfle + 1 if halfle != le / 2 else halfle] + n[:halfle][::-1]
        if mid == '-1':
            m_small = small

        temp = str(int(n[:halfle + 1 if halfle != le / 2 else halfle]) + 1)
        mid = str(int(n[halfle]) + 1) if halfle != le / 2 else ''
        big = temp[:-1 if mid else le] + mid + temp[::-1][1 if mid else 0:]
        if mid == '10':
            big = small
        res = {1: big, 2: small, 3: m_small}[{
            abs(int(big) - int(n)): 1, abs(int(n) - int(small)): 2, abs(int(n) - int(m_small)): 3
        }[min(abs(int(big) - int(n)), abs(int(n) - int(small)), abs(int(n) - int(m_small)))]]
        if n.endswith('0' * (le - 1)):
            res = str(int(res) - 2)
        elif n == '9' * le:
            res = str(int(n) + 2)
        if res == n:
            mid = int(n[halfle]) - 1
            if mid == -1:
                mid = 1
            res = n[:halfle] + str(mid) + n[:halfle][::-1]
        if n.endswith('1') and n.startswith('1') and n[1:-1] == '0' * (le - 2):
            res = str(int(n) - 2)
        return res
