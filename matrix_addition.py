r1 = input("Row 1")
c1 = input("Column 1")
r2 = input("Row 2")
c2 = input("Column 2")
if r1 == r2 and c1 == c2:
  a = []
  for i in xrange (r1):
    a.append([])
  b = []
  for i in xrange (r2):
    b.append([])
  for i in xrange (r1):
    for j in xrange(c1):
      num = input("Enter element :")
      a[i].append(num)
  for i in xrange (r2):
    for j in xrange(c2):
      num = input("Enter element :")
      b[i].append(num)
  s = []
  for i in xrange (r1):
    s.append([])
  for i in xrange (r1):
    for j in xrange (c1):
      s[i].append(a[i][j] + b[i][j])
  for i in xrange (r2):
    for j in xrange(c2):
      print s[i][j],
    print
else:
  print "Addition not possible"
