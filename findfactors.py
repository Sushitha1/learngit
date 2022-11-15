def findfactors(num):
    a=[]
    for i in range(1,num+1):
        if num % i == 0:
            a.append(i)
    return a
user=int(input("Give the no: "))
print("Factors of ",user," are ",findfactors(user))
fhand = open("data.txt","w")
str1=''
for i in findfactors(user):
    str1 = str1 + " " +str(i)
fhand.write(str1)
