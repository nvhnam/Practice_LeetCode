from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap, DesignHashSet, PathSum, TreeNode2, AddingNegaBinaryNumber, AddTwoNumbers, ThreeSum, TwoSum, LRUCache, QueueUsingStack, SubArraySumK, MostCommmonWord, PopulatingNextRightPointer, CustomSortString, SpiralMatrix, SwappingNodesLinkedList, ValidParentheses, ValidPalindromeII, ReverseWordsInString, KLargestInArray, DifferenceTwoArrays, MaxAvgSubArray, UniqueNumberOccur, MaxDepthBinary, ContainerMaxWater, NTribonaccyNum, RemovingStarFromString, IncreasingTripletSubsequence, ProductArrayExceptSelf, MaxVowelInSubString, MaxConsecutiveOneIII, DecodeString, IntToRoman, RomanToInt, TreeTraversal, TreeNode

def main():
    tree_traversal = TreeTraversal()
    root = TreeNode(1)
    # root.left = TreeNode(None)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(tree_traversal.inorderTraversal(root))

main()