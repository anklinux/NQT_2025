# Input : 7  -> Value of N [1,0,2,0,1,0,2]-> Element of arr[0] to arr[N-1],
# while input each element is separated by new line.
# Output : 0 0 0 1 1 2 2  -> Element after sorting based on risk severity 

#  using function method

def sort_by_risk(arr):
    return sorted(arr)

num = int(input())
arr = []

for i in range(num):
    arr.append(int(input()))
    
sorted_arr = sort_by_risk(arr)
print(*sorted_arr)    

# using sort method
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in sorted(arr):
    print(i, end = " ")
    
