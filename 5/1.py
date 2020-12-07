maxRow=0
maxSeat=0


data=open("./in","r")
for l in data:
    row=l[:7]
    seat=l[7:10]

    print("{} {}".format(row,seat));

    nrow=0
    nseat=0
    for i,b in enumerate(row):
        if b=='B':
            nrow+=2**(6-i)
        print("{} {} {}".format(i,b,nrow));

    for i,b in enumerate(seat):
        if b=='R':
            nseat+=2**(2-i)
        print("{} {} {}".format(i,b,nseat));

    if nrow>maxRow:
        maxRow=nrow
        maxSeat=nseat
    elif nrow==maxRow and nseat>maxSeat:
        maxSeat=nseat

data.close();

print("Row {} col {} seat {}".format(maxRow, maxSeat, maxRow*8+maxSeat))
