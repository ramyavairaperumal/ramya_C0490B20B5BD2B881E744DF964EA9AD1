def recursion_fact(x):
  if x==1:
    return 1
  else:
    return(x*recursion_fact(x-1))
num=int(input("Enter a number:"))
if num>=1:
  print("The factorial of",num,"is",recursion_fact(num))
  
