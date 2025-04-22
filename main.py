from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap, DesignHashSet, PathSum, TreeNode2, AddingNegaBinaryNumber, AddTwoNumbers, ThreeSum, TwoSum, LRUCache, QueueUsingStack, SubArraySumK, MostCommmonWord, PopulatingNextRightPointer, CustomSortString, SpiralMatrix, SwappingNodesLinkedList, ValidParentheses, ValidPalindromeII, ReverseWordsInString, KLargestInArray, DifferenceTwoArrays, MaxAvgSubArray, UniqueNumberOccur, MaxDepthBinary, ContainerMaxWater, NTribonaccyNum, RemovingStarFromString, IncreasingTripletSubsequence, ProductArrayExceptSelf, MaxVowelInSubString, MaxConsecutiveOneIII

def main():
    max_consecutive_one_iii = MaxConsecutiveOneIII()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(max_consecutive_one_iii.longestOnes(nums, k))

main()