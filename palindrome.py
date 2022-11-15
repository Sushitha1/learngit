def palindrome(user):
  if user[:] == user[::-1]:
    print("Its a palindrome")
  else:
    print("No,its not a palindrome")
u=input()
palindrome(u)