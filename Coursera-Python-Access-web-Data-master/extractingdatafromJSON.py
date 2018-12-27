from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter - ')
data= urlopen(url, context=ctx).read()
# print("data",data)

info = json.loads(data)

# print('information',info)
# print("count:",len(info))
sum=0
counts=0
for item in info['comments']: # to go to comment
     value= item['count']
     print('values',value)
     sum=sum+int(value)
     counts=counts+1
print('sum',sum)
#     print('Id', item['id'])
#     print('Attribute', item['x'])
