
def single_digit_sum(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n 
def solve(N,R):
    if R == 0:
        return 0
    digit_sum  = sum(int(d) for d in str(N))
    total  = digit_sum * R
    return single_digit_sum(total)

N = int(input())
R = int(input())

print(solve(N,R))    