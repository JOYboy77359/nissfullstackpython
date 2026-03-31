"""d={1:"A",2:"B",4:"C",3:"C"}
#print(d.setdefault(5))
#print(d)
print(d.setdefault(6,"F")) #setdefault
print(d)
# wap initize no 125 display all digit revorder
no=125
while no!=0:
	r=no%10
	print(r)
	no=no//10
no=125
s=0
while no!=0:
	r=no%10
	s=s*10+r
	no=no//10
print("revno=",s)
no=123
s=0
temp=no
while no!=0:
	r=no%10
	s=s*10+r
	no=no//10
if temp==s:
	print(temp,"is pd number")
else:
	print(temp,"is not pd number")
#wap intilize no 125 display first digit 
no = -125
if no < 0:
    no = -no
c=0
while no!=0:
    no = no // 10
    c=c+1
print("First digit:", no)"""
for i in range (1,4,1):
	for j in range(1,5,1):
		print(j,end="\t")
	print()