num=-12
flag=True
if(num<0):
    flag=False
    num=-num
#print(num)
l=len(str(num))
z=l
answer=0
#print(l)
for i in range(0,l):
    result=num%(10**(i+1))
    num=num-result
    #print(result)
    z=z-1
    powa=10**z
    final=(result*(powa))/(10**(i))
    answer=final+answer
if(flag==False):
    answer=-answer
print(int(answer))