a = input()
print(a.split()[0])

def split(target, num):
    return int(target.split()[num])

def nokori(percent):
    return round((100 - percent)/100,2)

print(split(a,0) * nokori(split(a,1)) * nokori(split(a,2)))