r = input("Row count :")
c = input("Column count :")
m = []
for n in xrange (r):
  m.append([])
for i in xrange (r):
  for j in xrange (c):
    ch = input("Enter value at ["+str(i)+"]["+str(j)+"] :")
    m[i].append(ch)
t = []
for i in xrange (c):
  t.append([])
for i in xrange (c):
  for j in xrange (r):
    t[i].append(m[j][i])
for k in xrange (c):
  for l in xrange (r):
    print t[k][l],
  print
