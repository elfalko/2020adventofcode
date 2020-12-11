ictr=0
acc=0

instr=[]

data=open("./in","r")
for l in data:
    line=l.split(" ")
    i=line[0]
    num=int(line[1])
    
    instr.append([i,num,0])
data.close();

def run():
    global ictr
    global acc
    global instr

    i=instr[ictr]

    print("Running {}: {}".format(ictr,i))

    # If i[2] == 1 we are done
    if i[2] >= 1:
        print(acc)
        return True
    else:
        instr[ictr][2]+=1
        if i[0]=='nop':
            ictr+=1
        elif i[0]=='jmp':
            ictr+=i[1]
        elif i[0]=='acc':
            acc+=i[1]
            ictr+=1
        else:
            print("Invalid instruction {} {}".format(ictr,i[0])) 
        return False

found=False
while not found:
    found=run()
