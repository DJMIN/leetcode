ex = {
    'I': 1,
    'IV': 3,
    'IX': 8,
    'V': 5,
    'X': 10,
    'XL': 30,
    'XC': 80,
    'L': 50,
    'C': 100,
    'CD': 300,
    'CM': 800,
    'D': 500,
    'M': 1000,

}


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        res += ex[s[0]]
        for index, ch in enumerate(s[]):
            temp = ex.get(s[index-1: index])
            res += temp if temp else ex[ch]

        return res