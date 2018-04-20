class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            '(':')',
            '[':']',
            '{':'}',
        }


        if not s:
            return True
        def retneibu(s):
            print(s)
            houwei = s.find(d.get(s[0], '1'))
            print(houwei)

            if houwei == 1:
                return True
            elif houwei > 1:
                if s:
                    flag = True
                    if houwei+1 < len(s):
                        flag = retneibu(s[houwei+1:])
                    return retneibu(s[1:houwei+1]) and flag
                else:
                    return True
            else:
                return False

        return retneibu(s)


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap:
                if parmap[c] != pars.pop():
                    return False
            else:
                pars.append(c)
        return len(pars) == 1



print(Solution().isValid("{{{[]}}}()"))
