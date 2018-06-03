histogram ={}
s = raw_input("Enter string :")
for ch in s:
  histogram[ch] = histogram.get(ch,0)+1
print histogram
