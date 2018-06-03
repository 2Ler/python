def binary_to_decimal(x):
  num = x
  decimal = 0
  i = 0
  while num != 0:
    r = num%10
    decimal += r * (2**i)
    num = num/10
    i+=1
  return decimal
s = input("Binary number :")
print binary_to_decimal(s)," is the decimal of ",s
