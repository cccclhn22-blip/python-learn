def bmi(w,h):
    return w/h**2
w=float(input("your weight:"))
h=float(input("your height:"))
result=bmi(w,h)
print(round(result,1))
     