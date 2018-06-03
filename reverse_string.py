s=raw_input()
reverse=""
for i in xrange(len(s)-1,-1,-1):
  reverse+=s[i]
print reverse
