class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        s = str(x)

        if "-" in s:
            print("hi")
            neg = True
            m = s.replace("-", '')

        if neg:
            l = list(m)
            l = reversed(l)
            rev = int(''.join(l))
            if -(2 ** 31) <= -abs(rev) <= 2 ** 31 - 1:
                return -abs(rev)
            else:
                return 0
        else:
            l = list(s)
            l = reversed(l)
            rev = int(''.join(l))
            if -(2 ** 31) <= rev <= 2 ** 31 - 1:
                return rev
            else:
                return 0

