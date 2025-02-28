# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D


a,b = map(int,input().split())
matrix = []
valid = True
for i in range(a):
    A = list(input())
    matrix.append(A)
for i in range(a):
    for j in range(b):
        if matrix[i][j] == "*":
            continue
        count = 0
        opt = [(0,-1),(0,1),(-1,0),(1,0),(-1,1),(-1,-1),(1,1),(1,-1)]
        for r,c in opt:
            if 0 <= r + i < a and 0<=j + c <b and matrix[r+i][c+j] == "*":
                count += 1
        if count and matrix[i][j] == ".":
            valid = False
        elif matrix[i][j] != "." and int(matrix[i][j]) != count:
            valid = False
if not valid:
    print("NO")
else:
    print("YES")