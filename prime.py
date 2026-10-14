count=0
for n in range (2,101):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
        count=count+1
print("total:",count)