from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap, DesignHashSet

def main():
    myHashSet = DesignHashSet()
    myHashSet.add(1)
    myHashSet.add(2)      
    myHashSet.contains(1)
    myHashSet.contains(3) 
    myHashSet.add(2)      
    myHashSet.contains(2) 
    myHashSet.remove(2)   
    myHashSet.contains(2) 
    myHashSet.getRandom()
    print(myHashSet)

main()