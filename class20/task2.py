import requests,json
response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()
print(type(users))

new_users=[]
for user in users:
    new_users.append({"id":user['id'],
                      'name':user['username'],
                      'city':user['address']['city'] })
print(new_users)


fp1=open('users.json','w')
json.dump(new_users,fp1)
print("new json file is created")