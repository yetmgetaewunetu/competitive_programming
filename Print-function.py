if __name__ == '__main__':
    n = int(input())
    List =  []
    for i in range(1, n+1):
        List.append(i)
    print(*List, sep = '')
