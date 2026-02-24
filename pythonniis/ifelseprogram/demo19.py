"""wap to take person h from keyboard check if the person is sligiable for voting or not
print("enter a age")
age=int(input())
if age>=18:
	print("Eligiable")
else:
	print("Not Eligiable")
	
print("enter a age")
age=int(input())
msg="eligiable" if age>=18 else "not eligiable"
print(msg)
"""
print("enter a number")
age=int(input())
msg="even" if age%2==0 else "odd"
print(msg)