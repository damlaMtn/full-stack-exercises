import requests

import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code

print(r.request.headers)

print("request body:", r.request.body)

header=r.headers
print(r.headers)

header['date']
header['Content-Type']

r.encoding

r.text[0:100]

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r=requests.get(url)

print(r.headers)

r.headers['Content-Type']

path=os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)

#------------GET------------------------

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}

r=requests.get(url_get,params=payload)

r.url

print("request body:", r.request.body)
print(r.status_code)
print(r.text)

r.headers['Content-Type']

r.json()

r.json()['args']

#------------POST------------------------

url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

r_post.json()['form']