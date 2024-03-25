class Solution:
    def value(self, r):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if dic.get(r) == None:
            return -1
        else:
            return dic.get(r)

    def romanToInt(self, s: str) -> int:
        res = 0
        if 'IV' in s:
            res = res + 4
            s = s.replace('IV', '')

        if 'IX' in s:
            res = res + 9
            s = s.replace('IX', '')

        if 'XL' in s:
            res = res + 40
            s = s.replace('XL', '')
        if 'XC' in s:
            res = res + 90
            s = s.replace('XC', '')
        if 'CD' in s:
            res = res + 400
            s = s.replace('CD', '')
        if 'CM' in s:
            res = res + 900
            s = s.replace('CM', '')

        for i in s:
            res = res + self.value(i)

        return res


