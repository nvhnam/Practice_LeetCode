from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap, DesignHashSet, PathSum, TreeNode2, AddingNegaBinaryNumber, AddTwoNumbers, ThreeSum, TwoSum, LRUCache, QueueUsingStack, SubArraySumK, MostCommmonWord, PopulatingNextRightPointer

def main():
    most_common_word = MostCommmonWord()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(most_common_word.mostCommonWord(paragraph, banned))

main()