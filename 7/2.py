mybag="shiny gold"

baglist=[]

directbags=[]
indirectbags=[]

data=open("./in","r")
for l in data:
    outer=l.split(" bags")[0]
    inner=l.split("contain ")[1].split(", ")
    innerbag=[]
    innernum=[]
    for entry in inner:
        num=entry.split(" ")[0]
        if num=='no':
            num=0
        else:
            num=int(num)
            innerbag.append(" ".join(entry.split(" bag")[0].split(" ")[1:]))
        
        innernum.append(num)
    
    baglist.append([outer,innernum,innerbag])


data.close();

for b in baglist:
    print(b)

def get_inner_bags(baglist,name,depth):
    subbags = 0
    # debugging
    dstr=">>"*depth
    if depth>0:
        dstr+=" "

    # find our entry
    for e,entry in enumerate(baglist):
        if entry[0].find(name) >= 0:
            print("{}Found {} {}".format(dstr, e, entry))
            # if no subbags, return
            if entry[1][0] == 0:
                return 1
            # if subbags
            else:
                # go through all
                for i,subbag in enumerate(entry[2]):
                    # call recursively to get subbags
                    contained=get_inner_bags(baglist,subbag,depth+1)
                    # get amount of this subbag
                    amount=int(entry[1][i])
                    csum=amount*(contained);
                    print("{}Returned from {}: {}x{} bags = {}".format(dstr,subbag,amount,contained,csum))
                    # add to our sum
                    subbags += csum 

    print("{}{:d} Subbags for {} done".format(dstr,subbags,name))
    return subbags + 1

print(get_inner_bags(baglist,mybag,0))
