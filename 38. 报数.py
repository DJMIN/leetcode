class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(2, n + 1):
            num = 1
            temps = ''
            for index, ch in enumerate(s[1:]):
                if ch == s[index]:
                    num += 1
                else:
                    temps += '%d%s' % (num, s[index])
                    num = 1
            if num:
                temps += '%d%s' % (num, s[-1])
            s = temps
            # li = [{'key': key, 'value': value} for key, value in data.items()]
            # li.sort(key=lambda x: x['key'])
            # for ii in li:
            #     s += '%d%d' % (ii['key'],ii['value'])
        return s

print(Solution().countAndSay(1))
