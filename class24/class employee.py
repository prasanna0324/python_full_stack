class Account:
 min_bal=500
 def __init__(self,id,name,amount):
  self.acc_id=id
  self.acc_name=name
  self.acc_bal=amount
e1=Account(101,"RG",5000)
print(e1.__dict__)
e2=Account(102,"SG",1500)
print(e2.__dict__)
e3=Account(103,"PG",25000)
print(e3.__dict__) 
print(Account.__dict__)  