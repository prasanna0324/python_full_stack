numbers=[1,2,3,4,5,6,7,8,9,10]
def verify(num):
    return num%2==0
even_nos=list(filter(lambda n:n%2==0,numbers))
print(even_nos)