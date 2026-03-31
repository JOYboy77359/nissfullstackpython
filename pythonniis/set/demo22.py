"""for i in range(68,64,-1):
	for j in range(i,69,1):
		print(j,end="\t")
	print()
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print(1)
for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()
for i in range(2,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()"""
n = 4

for i in range(n, 0, -1):
    # left increasing part
    for j in range(1, i + 1):
        print(j, end="")
    
    # spaces
    for k in range(2 * (n - i) - 1):
        print(" ", end="")
    
    # right decreasing part
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()