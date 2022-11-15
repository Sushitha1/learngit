user=input("Give a number: ")
arm=0
try:
    a=len(user)
    for i in range(a):
        arm= arm + int(user[i])**a
    print(arm)
except:
    print("Error please enter a number")