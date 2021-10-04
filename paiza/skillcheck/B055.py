import math
a = input()
inp = []
count = int(a.split()[0])
while count > 0:
    inp.append(input().split())
    count -= 1

ans_min = 0
ans_max = 0

for (line,i) in enumerate(inp):
    if ((int(a.split()[1]) - int(i[0])) / int(i[2])) % 1 == 0:
        ans = int(i[1]) + int(i[3]) * (math.ceil(((int(a.split()[1]) - int(i[0])) / int(i[2])))+1)
    else:
        ans = int(i[1]) + int(i[3]) * math.ceil(((int(a.split()[1]) - int(i[0])) / int(i[2])))

    if (line + 1) == 1:
        ans_min = ans
        ans_max = ans
    else:
        if ans >= ans_max:
            ans_max = ans
            # print(ans_max)
        elif ans <= ans_min:
            ans_min = ans


print(ans_min, end=" ")
print(ans_max)