import random

OP=[250,300,400,1000]
Time=[0,1,12,120]
def get_b_s()->tuple:
	return (random.random(),random.uniform(0.95,1))
def get_ssm(b=None,s=None):
	if b==None and s==None:
		b,s=get_b_s()
	print(b,s)
	print(b*s**0)
	print(15/(b*s**0)-15)
	ssm=0
	for i in range(3):
		ssm+=(250/(b*(s**Time[i+1]))-OP[i+1])**2
		print(ssm)
	return ssm,b,s
Min=10000
b=0
s=0
for i in range(999999):
	ssm=get_ssm()
	if ssm[0]<Min:
		Min=ssm[0]
		b=ssm[1]
		s=ssm[2]
print(Min,b,s)
