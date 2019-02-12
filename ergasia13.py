# ergasia 13
def maxDistanse(a,maximum):
	maxsum=0
	for i in range(0,len(a)):
		s=0
		for j in range(i,len(a)):
			if s+a[j]<=maximum:
				s+=a[j]
			else:
				break
			if s>maxsum:
				maxsum=s
	return maxsum

print("eisagete tis apostaseis stin lista gia na teleiosete patiste enan akeraio <=0")
lista=[0]  #ετσι εξασφαλιζετε οτι η'lista' δεν θα ειναι κενη
c=int(input('eisagete edo : '))
lista.append(c)
while c>0:
	c=int(input('eisagete edo : '))
	if c>0:
		lista.append(c)
	pass
d=int(input('eisagete tin megisti apostasi : '))
while d<=0:
	d=int(input('h megisti apostasi prepei na einai pragmatikos arithmos : '))
	pass
print("h megisti apostasi einai {0:10d} km".format(maxDistanse(lista,d)))
aa=input('press enter to finish')

