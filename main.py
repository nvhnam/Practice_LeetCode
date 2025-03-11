from Problems import MaxProfit, MergeSortedArrays, RemoveElements

def main():
    removeElement = RemoveElements()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(removeElement.remove_elements(nums, val))

main()