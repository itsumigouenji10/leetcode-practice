
def two_sum(nums, target):
    """
    Return indices of the two numbers in nums that add up to target.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int]: Indices [i, j] such that nums[i] + nums[j] == target.

    Raises:
        ValueError: If no such pair exists.
    """
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i] # Return seen first because it is an earlier index. As such the order the doesn't matter like they said but if it does matter
        else:
            seen[nums[i]] = i # Basically, insert the value, nums[i] and the index i into the hash map 
    
    # For the event that no target sum is found
    raise ValueError("No two indices have values that add up to the target")

if __name__ == "__main__":
    nums = [3,3,4,5,6,7,8,9]
    target = 60
    print("The two indices are: ", two_sum(nums, target))