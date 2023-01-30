#2884jun
H, M = map(int, input().split())
if M-45 < 0 and H>0:
    H1 = H-1 
    M1 = (60-45)+M
    print(H1,M1)

elif H -45 > 0 :
    M2 = M-45
    print(H, M2)

else: 
    M3 = M + 15
    print('23',M3)