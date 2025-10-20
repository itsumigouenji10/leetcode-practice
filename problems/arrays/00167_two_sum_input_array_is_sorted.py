def two_sum_sorted(numbers, target):

    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:  # Found the pair
            return [left + 1, right + 1]  # 1-indexed

    return []

def two_sum_brute(nums, target):
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            current_sum = nums[i] + nums[j]
            if current_sum == target:
                return [i+1,j+1] # Since the array is 1-indexed which implies that the indexing starts at 1 instead of 0, return i+1, j+1

    return []

if __name__ == "__main__":
    nums = [3,3,4,5,6,7,8,9]
    target = 6
    print("The two indices are: ", two_sum_brute(nums, target))
    print("The two indices are (optimized): ", two_sum_sorted(nums, target))