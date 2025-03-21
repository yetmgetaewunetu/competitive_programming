# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D


import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        w = input()
        def helper(i,j,ch):
            if ch=='z':
                return 0
            if i == j:
                if w[i] == ch:
                    return 0
                return 1
            mid = (j + i + 1)//2
            left = (j-i+1)//2 - w[i:mid].count(ch)
            left += helper(mid,j,chr(ord(ch) + 1))
            
            right = (j -i + 1)//2 - w[mid:j+1].count(ch)
            right += helper(i,mid - 1,chr(ord(ch)+1))
            
            return min(right,left)
        
        print(helper(0,n-1,'a'))


    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()










