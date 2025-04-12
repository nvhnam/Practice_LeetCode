from typing import List


class ContainerMaxWater:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            x = min(height[i], height[j])
            area =  x * (j - i)
            res = max(res, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res