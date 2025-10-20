"""
    [0026 - Remove Duplicates from a Sorted Array]
    Link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array
    Notes have been provided in a seperate folder '/notes'
"""
from collections import Counter

def remove_duplicates(nums):
    # This function contains the optimal solution
    # Initially I thought let's just use sets but then I remembered that set does not preserve order
    # Since we don't want that, our other solution was to use a hash map that keeps the count
    
    # Let's just handle the empty array test case right away
    if not nums:
        print("It's an empty list!")
        return 0, nums
    
    count = Counter(nums)
    unique = []

    for num in nums:
        if count[num] > 0:
            unique.append(num)
        count[num] = 0

    return len(unique), unique

def remove_duplicates_brute(nums):
    # This function contains the brute-force solution (trade-offs discussed in /notes folder)
    # Time complexity - O(n) 
    # Space complexity - O(k) since we use the exact same data structure
    # Simply looping over using for doesn't always consider all the duplicates and also can throw out of bounds error
    # Because of this using the same data structure isn't optimal so a new data structure is required
    # Which is why we used 'seen' as an array that only contains elements from nums that were not seen before

    # Let's just handle the empty array test case right away
    if not nums:
        print("It's an empty list!")
        return 0, nums
    
    seen = []
    for num in nums:
        if num not in seen:
            seen.append(num)

    return len(seen), seen

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