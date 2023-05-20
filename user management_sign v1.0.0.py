#user managment_sign_in/up:v.1.0.0
'''
user enters: name,familyname,age,username,password,passwordrepeat
user gets signed up

informationof new user gets saved in a file



user enters: username,password
user gets signed in if information is exist in the saved file 


'''


usersave= open('usersave.txt')
read=usersave.read()
list=read.split('\n')
database=[]
for line in list:
	parts=line.split('.')
	database+=[parts]
usersave.close()




import turtle as t
t.speed(100000)






mode=t.textinput('user sign','in for sign in, up for sign up')

def acpn(name):
	if name!='':
		return True
	else :
		return False
def acpf(family):
	if family != '':
		return True
	else:
		return False
def acpa(age):
	if age != '':
		return True
	else:
		return False	
def acpu(user):
	for d in database:
		if d[3]==user:
			return False
	if user != '':
		return True
	else :
		return False
		

def se(enck,p):
	num=0
	for i in enck:
		if i ==p:
			return str(num)
		num+=1

def enc(pas):
	enck='qweasdrtyf_@ghzxcuiojklvbnmp2610957438'
	cpas=''
	for p in pas:
		n=se(enck,p)
		cpas+=n
		cpas+='.'
	cpas = cpas[0:(len(cpas)-1)]
	return cpas
		
		
		
	


def sign_up():
	t.pu()
	t.fd(-350)
	t.pd()
	t.pencolor('limegreen')
	t.pensize(50)
	t.fd(700)
	t.pencolor('skyblue')
	t.pu()
	t.left(90)
	t.fd(150)
	t.right(90)
	t.fd(-625)
	t.pd()
	t.fd(75)
	t.pu()
	t.fd(50)
	t.pd()
	t.fd(75)
	t.pu()
	t.fd(50)
	t.pd()
	t.fd(75)
	t.pu()
	t.fd(50)
	t.pd()
	t.fd(75)
	t.pu()
	t.fd(50)
	t.pd()
	t.fd(75)
	t.pu()
	t.pencolor('green')
	t.fd(-575)
	name=t.textinput('user sign_up','your name')
	if name != '':
		t.pd()
		t.fd(75)
		t.pu()
		t.fd(50)
	if acpn(name)!=True:
		quit()
	family=t.textinput('user sign_up','your family name')
	if family != '':
		t.pd()
		t.fd(75)
		t.pu()
		t.fd(50)
	if acpf(family) != True:
		quit()
	age=t.textinput('user sign_up','how old are you')
	if age != '':
		t.pd()
		t.fd(75)
		t.pu()
		t.fd(50)
	if acpa(age)!= True:
		quit()
	user=t.textinput('user sign_up','what should we call you(username)')
	if user != '':
		t.pd()
		t.fd(75)
		t.pu()
		t.fd(50)
	if acpu(user)!= True:
		quit()
	pas=t.textinput('user sign_up','set a password')
	rpas=t.textinput('user sign_up','repeat your password')
	if pas != '' :
		if rpas != '':
			if pas==rpas:
				t.pd()
				t.fd(75)
				t.pu()
				t.fd(50)
	cpas = enc(pas)
	return name,family,age,user,cpas
	



def sign_in(database):
	t.color('skyblue')
	t.pensize(80)
	t.pu()
	t.fd(-250)
	t.pd()
	t.fd(175)
	t.pu()
	t.fd(150)
	t.pd()
	t.fd(175)
	t.pu()
	t.fd(-500)
	us=t.textinput('sign in','enter your user name')
	if us=='':
		quit()
	checks=False
	for i in database:
		if i[3]==us:
			t.pd()
			t.pencolor('limegreen')
			t.fd(175)
			checks=True
			here=i
			break
	if checks ==False:
		quit()
	enck='qweasdrtyf_@ghzxcuiojklvbnmp2610957438'
	ps=t.textinput('sign in','enter your password')
	cp=here[4]
	pas=''
	cp=cp.split(',')
	for te in cp:
		
		pas+=enck[int(te)]
	if pas != ps:
		quit()
	t.pu()
	t.fd(150)
	t.pd()
	t.fd(175)
		
		
		
	
	
	
	
	
	
	
	













if mode =='in':
	sign_in(database)
elif mode =='up':
	name,family,age,user,cpas=sign_up()
	usersave= open('usersave.txt','a')
	usersave.write('\n'+name+'.'+family+'.'+age+'.'+user+'.'+cpas)
	usersave.close()
	
	
	
	
	
	
	
else:
	quit()


t.done()
