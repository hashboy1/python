import re
import numpy

s="This is a number 234-235-22-423"
r=re.match(".+(\d+-\d+-\d+-\d+)",s)
print(r.group(1))

r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
print(r.group(1))


print(re.match(r"aa(\d+)","aa2343ddd").group(1))
print(re.match(r"aa(\d+?)","aa2343ddd").group(1))
print(re.match(r"aa(\d+)ddd","aa2343ddd").group(1) )
print( re.match(r"aa(\d+?)ddd","aa2343ddd").group(1))
