import string
sum = 0
f = open("input.txt","r")
for line in f:
  numlist = string.split(line)
  for num in numlist:
    sum += int(num)
f.close()
avg = sum / len(numlist)
print "The average of digits is ",avg
