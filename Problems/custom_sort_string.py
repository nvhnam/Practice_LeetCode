import collections


class CustomSortString:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        s_count = collections.Counter(s)

        print("s_count: ", s_count)

        for char in order:
            if char in s_count:
                res.extend([char] * s_count[char])
                del s_count[char]

        for char, count in s_count.items():
            res.extend([char] * count) 

        return "".join(res)