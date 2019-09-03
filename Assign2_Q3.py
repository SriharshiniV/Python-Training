import re
from collections import Counter
x=input("enter a string")
spl=re.findall('[^A-Za-z0-9]',x)
print(Counter(spl))