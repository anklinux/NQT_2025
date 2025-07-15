# Note : For violating the rule, vehicles would be fined as X Rs.
# Input : 4 -> Value of N
# {5,2,3,7} -> a[], Elements a[0] to a[N-1], during input each element is separated by a new line
# 12 -> Value of D, i.e. date 
# 200 -> Value of x i.e. fine
# Output : 600  -> total fine collected 
# Explanation:
# Date D=12 means , only an even number of vehicles are allowed. 
# Find will be collected from 5,3 and 7 with an amount of 200 each.
# Hence, the output = 600

def calculate_fine(n, vehicles, date, fine_amount):
    total_fine = 0
    
    for num in vehicles:
       if (date % 2 == 0 and num % 2 != 0) or (date % 2 != 0 and num % 2 == 0):
           total_fine += fine_amount
    return total_fine

n = int (input())
vehicles = [int(input()) for i in range(n)]
d = int(input())
x = int(input()) 

print(calculate_fine(n, vehicles, d, x))      