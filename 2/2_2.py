f=open("./in","r")
ok=0
bad=0
total=0
for x in f:
    total+=1
    # give me the first number
    parts=x.split("-")
    nmin=int(parts[0])
    # give me the second number
    parts=parts[1].split(" ")
    nmax=int(parts[0])
    # give me pw
    pw=parts[2]
    # give me letter
    parts=parts[1].split(":")
    letter=parts[0]
    print("{}: min {} max {} letter {} pw {}".format(total,nmin,nmax,letter,pw))

    matches=0
    # match counting
    if pw[nmin-1]==letter:
        matches+=1
    if pw[nmax-1]==letter:
        matches+=1

    #analyse
    if matches == 1:
        ok+=1
        print("ok")
    else:
        bad+=1
        print("bad")
    
print("ok: {}, bad: {}, total: {}".format(ok,bad,total)); 

f.close()
