import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
counts=0
url = input('Enter - ')
data= urlopen(url, context=ctx).read()

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print('count:', len(lst)) #count no. of comment tags

for item in lst:
    total=item.find('count').text
    # print('overall total',total)
    sum=sum+int(total)
    counts=counts+1
print('sum',sum)
