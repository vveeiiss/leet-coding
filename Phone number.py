class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
               '9': 'wxyz'}
        lis1 = []
        for i in digits:
            lis1.append(dic[i])
        n = len(digits)
        if n == 0:
            return []
        if n == 1:
            return list(dic[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        print(prev)
        fin = dic[digits[-1]]
        print(fin)
        anw = [s + c for s in prev for c in fin]
        return anw

