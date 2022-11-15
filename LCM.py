def LCM(x,y):
  if type(x) is int and type(y) is int :
    a=max(x,y)
    b=min(x,y)
    if a%b == 0 and a%a == 0:
        print("LCM:",a)
    else:
      z=a
      while True:
        z=z+1
        if z % a == 0 and z % b == 0:
            print("LCM: ",z)
        if z > (a*b):
            break
x=int(input())
y=int(input())
LCM(x,y)