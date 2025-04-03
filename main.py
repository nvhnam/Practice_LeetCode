from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap, DesignHashSet, PathSum, TreeNode2, AddingNegaBinaryNumber, AddTwoNumbers, ThreeSum, TwoSum, LRUCache, QueueUsingStack, SubArraySumK, MostCommmonWord, PopulatingNextRightPointer, CustomSortString, SpiralMatrix, SwappingNodesLinkedList, ValidParentheses, ValidPalindromeII, ReverseWordsInString, KLargestInArray

def main():
    k_largest = KLargestInArray()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(k_largest.findKthLargest(nums, k))

main()