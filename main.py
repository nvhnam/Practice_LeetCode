from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap, DesignHashSet, PathSum, TreeNode2, AddingNegaBinaryNumber, AddTwoNumbers, ThreeSum, TwoSum, LRUCache, QueueUsingStack

def main():
    myQueue = QueueUsingStack()
    myQueue.push(1)
    myQueue.push(2)
    myQueue.push(3)
    myQueue.push(4)
    print(myQueue.pop())
    myQueue.push(5)
    # print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.pop())
    print(myQueue.pop())
    # print(myQueue.empty())

main()