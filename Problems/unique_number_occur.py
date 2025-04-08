from typing import List
from collections import Counter

class UniqueNumberOccur:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = Counter(arr)
        res = set()
        for key, val in hash_map.items():
            res.add(val)
        return True if len(res) == len(hash_map.keys()) else False