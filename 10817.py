A, B, C = map(int, input().split())

if A >= 1 and B >= 1 and C >= 1 and A <= 100 and B <= 100 and C <= 100:
    number = [A, B, C]
    number.sort()
    print(number[1])


# 모범답안
n = map(int, input().split())
print(sorted(n, reverse = True)[1])
