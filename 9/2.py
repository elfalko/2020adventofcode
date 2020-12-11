nums=[]
pre=25

# get instr
data=open("./in","r")
for l in data:
    nums.append(int(l))
data.close();

# i: index of number to check
# nums: array of numbers
# pre: current number of 
def is_sum_of_pre(i):
    if i<pre:
        print("index {} too low, don't have enough predecessors (need {})".format(i,pre))
        return False
    
    num=nums[i]
    pres=nums[i-pre:i]
    
    for fi, first in enumerate(pres):
        for second in pres[fi+1:]:
            if first+second==num:
                # print ("{}={}+{}".format(num,first,second))
                return True
    

    
    print("no sum found for {}".format(num))
    return False

i=pre
while is_sum_of_pre(i):
    i+=1

notasum = nums[i]
print(notasum)

def findSet():
    for bi,base in enumerate(nums):
        total=base
        mini=base
        maxi=base

        for nxt in nums[bi+1:]:
            total+=nxt

            if mini>nxt:
                mini=nxt
            if maxi<nxt:
                maxi=nxt
           
            if total == notasum:
                print("Min: {} Max: {} Sum: {}".format(mini,maxi,mini+maxi))
                return
            elif total > notasum:
                break

findSet()

