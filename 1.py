a = []
print("Enter n:")
n = int(input())
print("Enter elements of array:")
for q in range(n):
	a.append(int(input()))
i = 0
lastplus = a[0]
while i < len(a):
		if (a[i]>lastplus):
			lastplus = a[i]
		i += 1
i = 0
dobutok = 1
while i < len(a):
	if a[i] == lastplus:
		break
	dobutok *= a[i]
	i += 1
print("Result: ", dobutok)