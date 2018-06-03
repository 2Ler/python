f1 = open("integers.txt","r")
f2 = open("even.txt","w")
f3 = open("odd.txt","w")
for line in f:
  num = int(line.strip())
  if num % 2 ==0:
    f2.wrie(str(num) + "\n")
  else:
    f3.wrie(str(num) + "\n")
f1.close()
f2.close()
f3.close()
