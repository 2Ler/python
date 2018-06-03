sum = 0
f = open("myfile.txt","w")
for i in xrange(10):
  f.write(str(i)+"\n")
f.close()
f = open("myfile.txt","r")
for line in f:
  sum += int(line.strip())
f.close()
print "The sum of digits is ",sum
