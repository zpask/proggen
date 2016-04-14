import random

asc = {1:1,2:2,3:3,4:4,5:5,6:6,7:7}
des = {1:1,2:7,3:6,4:5,5:4,6:3,7:2}
ter = {1:1,2:3,3:5,4:7,5:2,6:4,7:6}
sex = {1:1,2:6,3:4,4:2,5:7,6:5,7:3}
qua = {1:1,2:4,3:7,4:3,5:6,6:2,7:5}
qui = {1:1,2:5,3:2,4:6,5:3,6:7,7:4}

while True:
	num = raw_input("How many chords?\n")
	if num == "exit":
		break
	num = int(num)
	degs = [0]
	prog = []
	harm = random.randrange(1,7)
	
	thing = 0
	
	for i in range(0, num):
		if thing<7:
			if degs[len(degs)-1] == 1:
				thing = random.randrange(thing+1,8)
			else:
				thing = random.choice([1,random.randrange(thing+1,8),random.randrange(thing+1,8),random.randrange(thing+1,8),random.randrange(thing+1,8),random.randrange(thing+1,8),random.randrange(thing+1,8),])
			degs.append(thing)
		else:
			thing = 1
			degs.append(thing)
	del degs[0]
	
	for i in degs:
		if i != 1:
			if harm == 1:
				prog.append(asc[i])
			elif harm == 2:
				prog.append(des[i])
			elif harm == 3:
				prog.append(ter[i])
			elif harm == 4:
				prog.append(sex[i])
			elif harm == 5:
				prog.append(qua[i])
			elif harm == 6:
				prog.append(qui[i])
		else:
			prog.append(i)
			harm = random.randrange(1,7)
	print prog
