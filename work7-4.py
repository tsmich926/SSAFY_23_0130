def collatz():
    N = int(input())
    cnt=0
    while N != 1:
        if N%2 == 0:
            N = N//2
        else:
            N = (N*3)+1
        cnt += 1
        if cnt == 500:
            return -1
    return cnt

print(collatz())