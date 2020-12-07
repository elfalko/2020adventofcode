def count_trees(h,v):
    hpos=0
    trees=0
    skip=0

    f=open("./in","r")
    for x in f:
        if skip>0:
            skip-=1
        else:
            l=len(x)-1

            # print("{} {}".format(hpos,x[hpos]))
            if x[hpos] == "#":
                trees+=1
                # print("tree hit")
            
            skip=v-1
        
            hpos=(hpos+h)%l

    f.close()
    return(trees)

trees = count_trees(1,1) * count_trees(3,1) * count_trees(5,1) * count_trees(7,1) * count_trees(1,2)  
# trees = count_trees(3,1)
print(trees)
# trees = count_trees(1,2)
# print(trees)
