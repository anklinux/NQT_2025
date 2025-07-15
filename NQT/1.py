# Example 1 : N=8 and arr = [4,5,0,1,9,0,5,0].
# There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array

# Input :8  – Value of N
# [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline

# Output: 4 5 1 9 5 0 0 0       

n = int(input("Number of  input: ")) # Number of element
arr = []

# element reads
for i in range(n):
    num = int(input())
    arr.append(num)
    
# move non zero element
result = []
zero_count = 0
for num in arr:
    if num != 0:
        result.append(num)
    else:
        zero_count += 1
        
# Add all zero at the end
result += [0] * zero_count

print(*result)