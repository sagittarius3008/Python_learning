# 5 2 4 標準入力からfizzbuzz
N = input()
for i in range(int(N.split(" ")[0])):
    if (i+1) % int(N.split(" ")[1]) == 0 and (i+1) % int(N.split(" ")[2]) ==0:
        print("AB")
    elif (i+1) % int(N.split(" ")[1]) == 0:
        print("A")
    elif (i+1) % int(N.split(" ")[2]) == 0:
        print("B")
    else:
        print("N")