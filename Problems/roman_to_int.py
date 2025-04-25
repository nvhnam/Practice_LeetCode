class RomanToInt:
    def romanToInt(self, s: str) -> int:
        table = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and table.get(s[i]) < table.get(s[i + 1]):
                res -= table.get(s[i])
            else:
                res += table.get(s[i])
        return res