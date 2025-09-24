numbers=[1,2,3,4,5]
def addplus(n):
    return n+1
new_numbers=list(map(addplus, numbers))
print(new_numbers)