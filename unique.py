user= input()
if type(user) is str:
    s=[]
    s=user.split()
    unique=set()
    unique.update(s)
    print(unique)
else:
    print("Hello, wrong input")