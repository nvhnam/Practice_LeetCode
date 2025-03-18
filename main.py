from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode

def main():
    elements = [1,2,3,4,5,6]
    root = TreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    countTreeNodes = CountTreeNodes()
    print(countTreeNodes.countNodes(root))


main()