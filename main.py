from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap, DesignHashSet, PathSum, TreeNode2, AddingNegaBinaryNumber, AddTwoNumbers, ThreeSum, TwoSum, LRUCache

def main():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    lRUCache.get(2)    
    lRUCache.put(4, 4)
    lRUCache.get(1)    
    lRUCache.get(3)    
    lRUCache.get(4)

main()