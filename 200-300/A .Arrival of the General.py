import re
s = 'abc123 xyz666 lmn-11 def77'
re.sub(r'b([a-z]+)(d+)', r'21:', s)
print(s)