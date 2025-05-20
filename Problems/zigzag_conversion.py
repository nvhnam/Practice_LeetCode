class ZigzagConversion:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        rows = [[] for _ in range(numRows)]
        idx, d = 0, 1

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return "".join(rows)