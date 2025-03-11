from Problems import MaxProfit, MergeSortedArrays

def main():
    merge_sorted_arrays = MergeSortedArrays()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge_sorted_arrays.merge(nums1, m, nums2, n)

main()