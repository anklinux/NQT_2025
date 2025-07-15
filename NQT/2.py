# Constrains-1<=N<=100
# Input : 10  -> Integer
# Output : 5    -> result- Integer
# Explanation: Binary representation of 10 is 1010. After toggling the bits(1010), 
# will get 0101 which represents “5”. Hence output will print “5”.


num = int (input())

# finds of number of bits in num
bits = len(bin(num)) - 2 # subtract 2 for '0b'

mask = (1 << bits) - 1  # create a number 1 bits (1111) like 15

result = num ^ mask # toggle 

print(result)