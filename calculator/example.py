n=0.000000000000000000000000000011234
n='%.2E' % n

s=str(n)
base=""
power=""
f=False
for i in range(0,len(s)):
  if s[i]=='E':
      f=True
      continue
  if f:
      power+=s[i]
  else:
      base+=s[i]         


print(base,power)
