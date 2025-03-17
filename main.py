from Problems import MaxProfit, MergeSortedArrays, RemoveElements, RemoveDuplicateFromSortedArray, MajorityElement, KidsWithCandies, CanPlaceFlowers, ReverseVowels, SmallestInfiniteSet

def main():
    smallestInfiniteSet = SmallestInfiniteSet()
    print(smallestInfiniteSet)
    smallestInfiniteSet.addBack(2);    
    smallestInfiniteSet.popSmallest()
    smallestInfiniteSet.popSmallest() 
    smallestInfiniteSet.popSmallest() 
    smallestInfiniteSet.addBack(1)  
    smallestInfiniteSet.popSmallest()
    smallestInfiniteSet.popSmallest() 
    smallestInfiniteSet.popSmallest() 
    print(smallestInfiniteSet)

main()