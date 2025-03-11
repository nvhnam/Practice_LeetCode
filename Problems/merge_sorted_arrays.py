from typing import List

class MergeSortedArrays:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int)  -> None:   
        nums1[:] = sorted(nums1[:m] + nums2[:n])
        print(nums1)
            