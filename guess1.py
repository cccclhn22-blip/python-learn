import random
answer=random.randint(1,10)
tries = 0
while True:
    s=int(input("chose from 1-10"))
    tries=tries+1
    if s==answer:
        print("bingo", tries, "tries")
        break
    elif s>answer:
        print ("too big")
    else:
        print ("too small")
    