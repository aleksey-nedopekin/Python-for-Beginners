A=[3,4,2,1,0,8,9,-1,100,0]
max=A.pop()
while A:
	a=A.pop()
	if a>max:
		max=a
print ("max=", max)