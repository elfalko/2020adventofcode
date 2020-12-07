vert=1
hor=3
vpos=0
hpos=0

trees=0

f=open("./in","r")

for x in f:
    l=len(x)-1

    print("{} {}".format(hpos,x[hpos]))
    if x[hpos] == "#":
        trees+=1
        print("tree hit")
    
    vpos+=vert
    hpos=(hpos+hor)%l

print(trees)

f.close()
