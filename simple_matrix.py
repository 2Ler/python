r = input("Row count :")
c = input("Column count :")
m = []
for n in xrange (r):
  m.append([])
for i in xrange (r):
  for j in xrange (c):
    ch = input("Enter value at ["+str(i)+"]["+str(j)+"] :")
    m[i].append(ch)
for k in xrange (r):
  for l in xrange (c):
    print m[k][l],
  print
