#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then
#converting the extracted strings to integers and summing up the integers.
import re
fname= input("enter file name:")
fhandle=open(fname) #open actual file
# lst=list()
sum=0
for line in fhandle:
    line=line.rstrip()
    numbers=re.findall('([0-9]+)',line)
    if not numbers:
        continue
    else:
        for number in numbers:
            sum=sum+int(number)
print(sum)
