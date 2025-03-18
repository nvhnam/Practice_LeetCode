from typing import List


class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expect_sum = n*(n+1) // 2
        real_sum = sum(nums)

        return expect_sum - real_sum