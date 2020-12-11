instr=[]

# get instr
data=open("./in","r")
for l in data:
    line=l.split(" ")
    i=line[0]
    num=int(line[1])
    
    instr.append([i,num])
data.close();

def run_instr(ictr,acc,cctr):
    i=instr[ictr]

    print("Running {}: {}".format(ictr,i))

    itemp=i[0]

    # exchange instr on the fly
    if ictr==cctr:
        if itemp=='nop':
            itemp='jmp'
        elif itemp=='jmp':
            itemp='nop'
        print("Switching instruction to {}".format(itemp))

    if itemp=='nop':
        ictr+=1
    elif itemp=='jmp':
        ictr+=i[1]
    elif itemp=='acc':
        acc+=i[1]
        ictr+=1
    else:
        print("Invalid instruction {} {}".format(ictr,itemp)) 
    return (ictr,acc)

def run_set(cctr):
    print("SET: Switching instruction {}".format(cctr))
    ictr=0
    acc=0
    l=len(instr)

    irep=[0]*l
    while True:
        if ictr>=l:
            # we terminated fuck yeah
            print(acc)
            return True
        else:
            if irep[ictr]>=1:
                #loop found
                break
            else:
                irep[ictr]+=1

                ictr, acc=run_instr(ictr,acc,cctr)
                print("ICTR {} ACC {}".format(ictr,acc))
    return False

for i in range(0,len(instr)-1):
    if run_set(i):

        break
