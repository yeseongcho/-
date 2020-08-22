n = 7
for i in range(n):

  if i == 0:

   print(" "*(n-1-i) + "*"+" "*(i+1))

  elif i == n-1:

   print("*" * (n*2-1))

  else:

   print(" "*(n-1-i) + "*"+" "*(i+1))
