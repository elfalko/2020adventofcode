mybag="shiny gold"

baglist=[]

directbags=[]
indirectbags=[]

options=1;


data=open("./in","r")
for l in data:
    outer=l.split("bags")[0]
    inner=l.split("contain ")[1].split(",")
    baglist.append([outer,inner])

    for bag in inner:
        if bag.find(mybag)>0:
            print(outer)
            directbags.append(outer)

data.close();

for package in directbags:
    for wrapper in baglist:
        for contents in wrapper[1]:
            if contents.find(package)>1 and wrapper[0] not in indirectbags and wrapper[0] not in directbags:
                indirectbags.append(wrapper[0])
                print(wrapper[0])

for i in range(5):
    for package in indirectbags:
        for wrapper in baglist:
            for contents in wrapper[1]:
                if contents.find(package)>1 and wrapper[0] not in indirectbags and wrapper[0] not in directbags:
                    indirectbags.append(wrapper[0])
                    print(wrapper[0])


print('{} {} {}'.format(len(directbags),len(indirectbags),len(directbags)+len(indirectbags)))



