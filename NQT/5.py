# Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.
# Note : 1st element of the array should be considered in the count of the result.
# For example, Arr[]={7,4,8,2,9}
# As 7 is the first element, it will consider in the result.
# 8 and 9 are also the elements that are greater than all of its previous elements.
# Since total of  3 elements is present in the array that meets the condition.
# 7 → count = 1 (first element)
# 4 → not greater than 7
# 8 → greater than 7 → count = 2
# 2 → not greater than 8
# 9 → greater than 8 → count = 3
# Hence the output = 3.
# Example 1: Input  7,4,8,2,9
# Output : 3

def count_greater_than_previous(arr):
    count = 1 # First element is always count
    max_so_far = arr[0]
    
    for num in arr[1:]:
        if num > max_so_far:
            count += 1
            max_so_far = num
        
    return count
    
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
print(count_greater_than_previous(arr))        