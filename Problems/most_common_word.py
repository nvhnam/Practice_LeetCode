from typing import List


class MostCommmonWord:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        table = {}
        norm_word = "".join(char.lower() if char.isalnum() else " " for char in paragraph)
        for p in norm_word.split():
            if p not in banned:
                if p not in table:
                    table[p] = 1
                else:
                    table[p] += 1
        # print(table)
        # print(norm_word)
        return max(table, key=table.get)