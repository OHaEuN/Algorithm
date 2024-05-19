import sys
inputf = sys.stdin.readline

st1 = list(inputf().strip())
st2 = []
M = int(inputf())

for _ in range(M):
	command = list(inputf().split())
	if command[0] == 'L':
		if st1:
			st2.append(st1.pop())
	elif command[0] == 'D':
		if st2:
			st1.append(st2.pop())
	elif command[0] == 'B':
		if st1:
			st1.pop()
	else:
		st1.append(command[1])
        
st1.extend(reversed(st2))
print(''.join(st1))