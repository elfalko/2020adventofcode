answers=[0 for i in range(26)] 
total=0
groupsize=0

data=open("./in","r")
for l in data:
    if l=="\n":
        print("[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]")
        print(answers)
        # new group starts, sum up old one
        groupAnswers=0
        if groupsize > 0:
            for a in answers:
                if a==groupsize:
                    groupAnswers+=1
            total+=groupAnswers
        print(groupAnswers)
        answers=[0 for i in range(26)] 
        groupsize=0

    else:
        answer=l.split("\n")[0]
        print(answer)
        for letter in answer:
            nletter=ord(letter) - 97
            # print("{} {}".format(letter,nletter))
            if nletter >= 0 and nletter < 26:
                answers[nletter]+=1
        groupsize+=1

data.close();

print(total)
