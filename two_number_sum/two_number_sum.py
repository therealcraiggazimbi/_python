numbers = [3,5,-4,8,11,1,-1,6]
sum = 10

#o(n^2) time | o(1) space
# def two_number_sum(array, target_sum):
#     for i in range(len(array) - 1):
#         first_num = array[i]
#         for j in range(i + 1, len(array)):
#             second_num = array[j]
#             if first_num + second_num == target_sum:
#                 return [first_num, second_num]
#     return []

# o(n) time | o(n) space
def two_number_sum(array, target_sum):
    nums = {}
    for num in array:
        potentialMatch = target_sum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# O(nlog(n)) | O(1) space
# def two_number_sum(array, target_sum):
#     array.sort()
#     left = 0;
#     right = len(array) - 1
#     while left < right:
#         current_sum = array[left] + array[right]
#         if current_sum == target_sum:
#             return [array[left], array[right]]
#         elif current_sum < target_sum:
#             left +=1
#         elif current_sum > target_sum:
#             right -=1

#     return []


print(two_number_sum(numbers,sum))