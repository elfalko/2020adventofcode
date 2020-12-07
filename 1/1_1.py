f=open("./in","r")
numbers = []
for x in f:
    numbers.append(int(x))
f.close()
found=False
for a in numbers:
    if found:
        break
    for b in numbers:
        if a+b < 2020:
            for c in numbers:
                s=a+b+c
                if s == 2020:
                    print(a*b*c)
                    found=True
                    break
f.close()
