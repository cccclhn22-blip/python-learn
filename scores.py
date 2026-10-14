parts=input("5 scores:").split(" ")
score=[]
for s in parts: 
    score.append(int(s))
score.sort(reverse=True)
print(score)