import cmath
print "Quadratic equation has form ax^2 + bx + c"
a = input()
b = input()
c = input()
d = (b * b) - (4 * a * c)
if d == 0:
  x = (-b) / (2 * a)
  print "Roots are x1=",x," x2="x
elif d > 0:
  x1 = (-b + (d ** .5)) / (2 * a)
  x2 = (-b - (d ** .5)) / (2 * a)
  print "Roots are x1=",x1," x2="x2
else:
  x1 = (-b + cmath.sqrt(d)) / (2 * a)
  x2 = (-b - cmath.sqrt(d)) / (2 * a)
  print "Roots are x1=",x1," x2="x2
