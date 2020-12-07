maxRow=0
maxSeat=0
maxI=(2**10)-1

seating=[False for i in range(maxI)] 


data=open("./in","r")
for l in data:
    row=l[:7]
    seat=l[7:10]

    # print("{} {}".format(row,seat));

    nrow=0
    nseat=0
    for i,b in enumerate(row):
        if b=='B':
            nrow+=2**(6-i)
        # print("{} {} {}".format(i,b,nrow));

    for i,b in enumerate(seat):
        if b=='R':
            nseat+=2**(2-i)
        # print("{} {} {}".format(i,b,nseat));

    seating[nrow*8+nseat]=True
    # if nrow>maxRow:
    #     maxRow=nrow
    #     maxSeat=nseat
    # elif nrow==maxRow and nseat>maxSeat:
    #     maxSeat=nseat

data.close();

for i,seat in enumerate(seating):
    # print("{} {}".format(i,seat));
    if i>0 and i<maxI:
        if seating[i-1]==True and seating[i+1]==True and seat==False:
            print(i)

# print("Row {} col {} seat {}".format(maxRow, maxSeat, maxRow*8+maxSeat))
