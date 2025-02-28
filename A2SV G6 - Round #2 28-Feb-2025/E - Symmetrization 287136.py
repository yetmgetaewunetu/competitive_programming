# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())

for _ in range(t):
    n =int(input())
    r,c = n//2,n//2
    count = 0
    if n %2:
        c += 1
    temp  = [list(input()) for i in range(n)]
    for i in range(r):
        for j in range(c):
            opts = [(i,j),(j,n-i-1),(n-i-1,n-j-1),(n-j-1,i)]
            zeros,ones = 0,0
            for l,k in opts:
                if temp[l][k] == "0":
                    zeros += 1
                else:
                    ones += 1
            count += min(zeros,ones)
    print(count)