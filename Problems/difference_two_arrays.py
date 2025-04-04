from typing import List


class DifferenceTwoArrays:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        only_1 = self.getElementsFromFirstList(nums1, nums2)
        only_2 = self.getElementsFromFirstList(nums2, nums1)
        return [only_1, only_2]

    def getElementsFromFirstList(self, nums1, nums2):
        hash_set = set(nums2)
        
        only_in_nums1 = set()
        for i in nums1:
            if i not in hash_set:
                only_in_nums1.add(i)
            
        return list(only_in_nums1)