cnt = int(input())
ans = 0

for i in range(cnt):
    [kamoku, eng, math, sci, read, his] = input().split()
    if int(eng) + int(math) + int(sci) + int(read) + int(his) >= 350:
        if kamoku == "s" and int(math) + int(sci) >= 160:
            ans += 1
        if kamoku == "l" and int(read) + int(his) >= 160:
            ans += 1


print(ans)