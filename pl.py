#수 출력
# class Person:
#     cnt=0
#     def __init__(self, name):
#         self.name = name
#         Person.cnt += 1

# person1 = Person('룰루')
# person1 = Person('랄라')
# print(Person.cnt)

# def collatz():
#     N = 0
#     cnt = 0
#     N = int(input())
#     while N != 1:
#         if N%2 == 0:
#             N = N//2
#         else:
#             N = (N*3)+1
#         cnt += 1 
#     return cnt


#? 원하는 수를 입력할때까지 입력받음
# def collatz():
#     N = 0
#     while N != 1:
#         N = int(input())
# collatz()


# N = int(input())
# cnt=0
# while N != 1:
#     if N%2 == 0:
#         N = N//2
#     else:
#         N = (N*3)+1
#     cnt += 1
#     if cnt == 500:
#         print(-1)
# print(cnt)


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