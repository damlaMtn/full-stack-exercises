### RandomUser API

#!pip install randomuser
#!pip install pandas

from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_list = r.generate_users(10)
some_list

name = r.get_full_name()

for user in some_list:
    print (user.get_full_name()," ",user.get_email())

for user in some_list:
    print (user.get_picture())

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)

get_users()

df1 = pd.DataFrame(get_users())


#--------------------------------------------------------------------------


### FruityVice API

import requests
import json

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

pd.DataFrame(results)

df2 = pd.json_normalize(results)
df2

cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

banana = df2.loc[df2["name"] == 'Banana']
(banana.iloc[0]['nutritions.calories'])



#--------------------------------------------------------------------------



### OfficialJoke API

data = requests.get("https://official-joke-api.appspot.com/jokes/ten")

results = json.loads(data.text)

df3 = pd.DataFrame(results)
df3.drop(columns=["type","id"],inplace=True)
df3

