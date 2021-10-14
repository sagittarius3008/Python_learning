x, y, r = [int(s) for s in input().split()]
con = int(input())

for i in range(con):
    a, b = [int(s) for s in input().split()]
    if (x-a)**2 + (y-b)**2 >= r**2:
        print("silent")
    else:
        print("noisy")