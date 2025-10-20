"""
    [0026 - Remove Duplicates from a Sorted Array]
    Link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array
    Notes have been provided in a seperate folder '/notes'
"""

def remove_duplicates(nums):
    # This function contains the optimal solution
    # Time complexity: O(n), Space complexity: O(1)
    # The pattern is Two pointers so we use writer and reader pointers to keep a track of the unique value
    if not nums:
        print("It's an empty list!")
        return 0, nums

    w = 0
    for r in range(1, len(nums)):
            if nums[r] != nums[w]:      # found a new unique
                w += 1
                nums[w] = nums[r]  

    return w+1, nums[0:w+1]  

def remove_duplicates_brute(nums):
    # This function contains the brute-force solution (trade-offs discussed in /notes folder)
    # Time complexity - O(n^2) 
    # Space complexity - O(1) since we use the exact same data structure

    # Let's just handle the empty array test case right away
    if not nums:
        return 0, nums

    i = 0
    # keep checking until the element just before the last one
    while i < len(nums) - 1:
        # if a duplicate run starts here
        if nums[i] == nums[i + 1]:
            val = nums[i]
            # remove every extra copy of that value
            while i + 1 < len(nums) and nums[i + 1] == val:
                del nums[i + 1]
        else:
            i += 1

    return len(nums), nums

if __name__ == "__main__":
    nums = [2,2,2,3,3,4,4,4,4,4,5,6,6,6,7,8]
    check = int(input("Enter 0 or 1 [0 for brute-force solution] and [1 for optimal]: "))
    if check:
        len_nums, nums = remove_duplicates(nums)
        print("The number of unique items in nums array [optimal] are: ", len_nums)
        print("The unique elements in nums are [optimal]:", nums)
    else:
        len_nums, nums = remove_duplicates_brute(nums)
        print("The number of unique items in nums array [brute] are: ", len_nums)
        print("The unique elements in nums are [brute]: ", nums)