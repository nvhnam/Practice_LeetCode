class ReverseWordsInString:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        stack = []
        for i in words:
            stack.append(i)
        while stack:
            res.append(stack.pop())

        return " ".join(res)