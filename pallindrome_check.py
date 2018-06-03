def is_pallindrome(str):
  n = len(str)
  if n ==1 :
    return True
  elif str[0] != str[n-1]:
    return False
  else:
    return is_pallindrome(str[1:n-1])
s = raw_input()
result = is_pallindrome(s)
if result == True:
  print "It is pallindrome"
else:
  print "It is not a pallindrome"
