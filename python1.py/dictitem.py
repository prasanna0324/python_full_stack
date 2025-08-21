emp={
    'eid':101,
    'ename':'sree',
    'esal':45000,
    'email':"sree@gmail.com",
    'email':"sree@ibm.com"
}
print(emp)

print(emp['ename'])
print(emp['eid'])
emp['ename']='Teja'
emp['esal']=50,000
emp['avail']=True
print(emp)

del emp['email']
emp['esal']
print(emp)