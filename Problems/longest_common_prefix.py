class LongestCommonPrefix:
    def longest_common_prefix(self, strs: list[str]) -> str:
        self.strs = strs

        the_strings = self.strs
        res = ""
        for i in range(len(the_strings[0])):
            for s in the_strings:
                if i == len(s) or s[i] != the_strings[0][i]:
                    return res
            res += the_strings[0][i]
        return res