def fibonacci(n):
    i=0
    new=1
    old=0
    while True:
        res=new+old
        old=new
        new=res
        print(res)
        i+=1
        if i > n:
            break
n=int(input())
fibonacci(n)