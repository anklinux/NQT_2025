# A supermarket maintains a pricing format for all its products. A value N is printed on each product.
# When the scanner reads the value N on the item, the product of all the digits in the value N is the
# price of the item. The task here is to design the software such that given the code of any item N the
# product (multiplication) of all the digits of value should be computed(price).
# Input : 5244 -> Value of N
# Output : 160 -> Price 
# Explanation: From the input above 
# Product of the digits 5,2,4,4
# 5*2*4*4= 160 , Hence, output is 160.

n = input()
p = 1

for i in n:
    p *= int(i)
print(p)     

def calculate_price(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

n = int(input("Enter a code "))
print(calculate_price(n))    