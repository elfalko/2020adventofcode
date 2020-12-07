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

    #analyse
    nletter=pw.count(letter);
    if nletter <= nmax and nletter >= nmin:
        ok+=1
    else:
        bad+=1
    
print("ok: {}, bad: {}, total: {}".format(ok,bad,total)); 

f.close()
