# ergasia 2
a=int(input("eisagete enan akeraio: "))
listt=[a]
i=0
b=len(listt)
while  i<b:
	j=2
	while j < listt[i]:
		if  listt[i]%j==0: 
			listt.append(j)
			listt.append(listt[i]//j)
			listt.remove(listt[i])
			b=len(listt)
			i=0
		else:
			j+=1
	pass
	i+=1
pass
print(listt)
c=input("press enter to finish")
