# ergasia 4
def plus(b):
	return '+'+str(b)

def minus(b):
	return '-'+str(b)

def times(b):
	return '*'+str(b)



def zero(a):
	if a[0]== '+':
		return int(a[1])
	elif a[0]== '-':
		return -int(a[1])
	else : 
		return 0

def one(a):
	if a[0]== '+':
		return 1+int(a[1])
	elif a[0]== '-':
		return 1-int(a[1])
	elif a[0]=="*" : 
		return 1*int(a[1])
	else:
		return 1

def tow(a):
	if a[0]== '+':
		return 2+int(a[1])
	elif a[0]== '-':
		return 2-int(a[1])
	elif a[0]=="*" : 
		return 2*int(a[1])
	else:
		return 2

def three(a):
	if a[0]== '+':
		return 3+int(a[1])
	elif a[0]== '-':
		return 3-int(a[1])
	elif a[0]=="*" : 
		return 3*int(a[1])
	else:
		return 3

def four(a):
	if a[0]== '+':
		return 4+int(a[1])
	elif a[0]== '-':
		return 4-int(a[1])
	elif a[0]=="*" : 
		return 4*int(a[1])
	else:
		return 4

def five(a):
	if a[0]== '+':
		return 5+int(a[1])
	elif a[0]== '-':
		return 5-int(a[1])
	elif a[0]=="*" : 
		return 5*int(a[1])
	else:
		return 5

def six(a):
	if a[0]== '+':
		return 6+int(a[1])
	elif a[0]== '-':
		return 6-int(a[1])
	elif a[0]=="*" : 
		return 6*int(a[1])
	else:
		return 6
def seven(a):
	if a[0]== '+':
		return 7+int(a[1])
	elif a[0]== '-':
		return 7-int(a[1])
	elif a[0]=="*" : 
		return 7*int(a[1])
	else:
		return 7

def eight(a):
	if a[0]== '+':
		return 8+int(a[1])
	elif a[0]== '-':
		return 8-int(a[1])
	elif a[0]=="*" : 
		return 8*int(a[1])
	else:
		return 8

def nine(a):
	if a[0]== '+':
		return 9+int(a[1])
	elif a[0]== '-':
		return 9-int(a[1])
	elif a[0]=="*" : 
		return 9*int(a[1])
	else:
		return 9
answer='1'
while answer == '1':
	
	c=input('kaleste thn sinaryisi edo : ')
	leftbrackets=[]
	rightbrackets=[]
	# στις 2 προηγουμενες λιστες θα αποθηκευονται οι θεσεις των δεξιων και αριστερων παρενθεσεων της μεταβλητης c
	for  i in range(0,len(c)):
		if c[i] == '(':
			leftbrackets.append(i)
		elif c[i] == ')' :
			rightbrackets.append(i)

	flag1=0
	flag2=0
	# με τις flag1 και flag2 στην συνεχεια θα ελενχετε αν η συναρτηση εχει κληθει σωστα απο τον χρηστη
	ch=''

	if len(leftbrackets) ==1 and len(rightbrackets) ==1:
		if c[0:leftbrackets[0]] =='zero':
			print(zero("  "))
			flag1=1
		elif c[0:leftbrackets[0]] =='one':
			print(one("  "))
			flag1=1
		elif c[0:leftbrackets[0]] =='tow':
			flag1=1
			print(tow("  "))
		elif c[0:leftbrackets[0]] =='three':
			flag1=1
			print(three("  "))
		elif c[0:leftbrackets[0]] =='four':
			flag1=1
			print(four("  "))
		elif c[0:leftbrackets[0]] =='five':
			flag1=1
			print(five("  "))
		elif c[0:leftbrackets[0]] =='six':
			flag1=1
			print(six("  "))
		elif c[0:leftbrackets[0]] =='seven':
			flag1=1
			print(seven("  "))
		elif c[0:leftbrackets[0]] =='eight':
			flag1=1
			print(eight("  "))
		elif c[0:leftbrackets[0]] =='nine':
			flag1=1
			print(nine("  "))
		flag2=1

	if len(leftbrackets) ==3 and len(rightbrackets) ==3:
		if c[leftbrackets[0]+1:leftbrackets[1]]=='plus':
			ch='+'
		elif c[leftbrackets[0]+1:leftbrackets[1]]=='minus':
			ch='-'
		elif c[leftbrackets[0]+1:leftbrackets[1]]=='times':
			ch='*'

		if  c[leftbrackets[1]+1:leftbrackets[2]]=='zero':
			ch = ch+'0'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='one':
			ch = ch+'1'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='tow':
			ch = ch+'2'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='three':
			ch = ch+'3'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='four':
			ch = ch+'4'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='five':
			ch = ch+'5'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='six':
			ch = ch+'6'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='seven':
			ch = ch+'7'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='eight':
			ch = ch+'8'
		elif c[leftbrackets[1]+1:leftbrackets[2]]=='nine':
			ch = ch+'9'

		if len(ch)==2:
			if (ch[0]=='+' or ch[0]=='-' or ch[0]=='*') and int(ch[1])<=9 and int(ch[1])>=0:
				flag1=1

		if flag1==1:
			if c[0:leftbrackets[0]] =='zero':
				print(zero(ch))
				flag2=1
			elif c[0:leftbrackets[0]] =='one':
				print(one(ch))
				flag2=1
			elif c[0:leftbrackets[0]] =='tow':
				flag2=1
				print(tow(ch))
			elif c[0:leftbrackets[0]] =='three':
				flag2=1
				print(three(ch))
			elif c[0:leftbrackets[0]] =='four':
				flag2=1
				print(four(ch))
			elif c[0:leftbrackets[0]] =='five':
				flag2=1
				print(five(ch))
			elif c[0:leftbrackets[0]] =='six':
				flag2=1
				print(six(ch))
			elif c[0:leftbrackets[0]] =='seven':
				flag2=1
				print(seven(ch))
			elif c[0:leftbrackets[0]] =='eight':
				flag2=1
				print(eight(ch))
			elif c[0:leftbrackets[0]] =='nine':
				flag2=1
				print(nine(ch))	


	if flag1 == 0 | flag2 == 0:
		print('h sinartisi den klithike sosta')
	answer=input("an thelete na epanalavete tin diadikasia patiste to 1 allios patiste kati allo")
	pass
aa=input("press enter to finish")	























