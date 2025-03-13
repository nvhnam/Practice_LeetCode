from typing import List


class KidsWithCandies:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        for i in range(len(candies)):
            new_num = candies[i] + extraCandies
            if new_num >= max(candies):
                results.append(True)
            else:
                results.append(False)
        
        return results