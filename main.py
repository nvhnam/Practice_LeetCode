from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet, AsteroidCollision, BinaryGap, SearchInsertPosition, MissingNumber, CountTreeNodes, TreeNode, DiagonalTraverse, DesignHashmap

def main():
    myHashMap = DesignHashmap()
    myHashMap.put(1, 1) 
    myHashMap.put(2, 2)
    myHashMap.get(1)
    myHashMap.get(3)    
    myHashMap.put(2, 1)
    myHashMap.get(2)
    print(myHashMap)
    myHashMap.remove(2)
    myHashMap.get(2)


main()