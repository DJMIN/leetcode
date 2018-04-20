def longestCommonPrefix(strs):
    res = ''
    if not strs:
        return res
    for i in range(0, len(strs[0])):
        temp_ch = strs[0][i]
        for s in strs[1:]:
            if i > len(s) -1 or s[i] != temp_ch:
                return res
        res += temp_ch
    return res

longestCommonPrefix(['sdfds', 'dfd', 'rtr'])