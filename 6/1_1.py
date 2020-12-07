answers=[0 for i in range(26)] 
total=0

data=open("./in","r")
for l in data:
    if l=="\n":
        # print(answers)
        # new group starts, sum up old one
        groupAnswers=0
        for a in answers:
            if a:
                groupAnswers+=1
        total+=groupAnswers
        print(groupAnswers)
        answers=[False for i in range(26)] 

    else:
        answer=l.split("\n")[0]
        for letter in answer:
            nletter=ord(letter) - 97
            print("{} {}".format(letter,nletter))
            if nletter >= 0 and nletter < 26:
                answers[nletter]+=1;

data.close();

print(total)
