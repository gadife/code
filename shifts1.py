import random

alephs = [["aleph1",0], ["aleph2",0], ["aleph3",0], ["aleph4",0], ["aleph5",0], ["aleph6",0]]
bets = [["bet1",0], ["bet2",0], ["bet3",0], ["bet4",0], ["bet5",0], ["bet6",0]]
alephs_r = [["aleph1",0], ["aleph2",0], ["aleph3",0], ["aleph4",0], ["aleph5",0], ["aleph6",0]]
bets_r = [["bet1",0], ["bet2",0], ["bet3",0], ["bet4",0], ["bet5",0], ["bet6",0]]
gimels = ["gimel1","gimel2","gimel3","gimel4","gimel5","gimel6"]
shifts = []
shifts_b = []
shifts_r = []
shits_all = [[]]

count = 6
count2 = 6
temp2 = 0
#for a in range(0,30):
#	count2 = 6
#	print "Day - ",a,count2
#	while count2 > 0:
#		temp = random.randrange(0,count)
#		#print alephs[temp][1]
#		if alephs[temp][1] == temp2:
#			alephs[temp][1] = alephs[temp][1] + 1
#			count2 = count2 -1
#			print alephs[temp], count2
#	temp2 = temp2 + 1



for a in range(0,30):
	found = False
	while not found:
		temp = random.randrange(0,6)
		if count2 == 0:
			count2 = 6
			temp2 = temp2 + 1
		if alephs[temp][1] == temp2:
				if a > 1 and (shifts[a-1] != alephs[temp][0] and shifts[a-2] != alephs[temp][0]):
					alephs[temp][1] = alephs[temp][1] + 1
					count2 = count2 - 1
					print "Day ",a,alephs[temp]
					shifts.append(alephs[temp][0])
					found = True
				if a == 0:
					alephs[temp][1] = alephs[temp][1] + 1
					count2 = count2 - 1
					print "Day ",a,alephs[temp]
					shifts.append(alephs[temp][0])
					found = True	
				if a == 1 and shifts[a-1] != alephs[temp][0]:
					alephs[temp][1] = alephs[temp][1] + 1
					count2 = count2 - 1
					print "Day ",a,alephs[temp]
					shifts.append(alephs[temp][0])
					found = True								

#print "DONE!!! with Aleph ", shifts
count = 6
count2 = 6
temp2 = 0
for b in range(0,30):
	found = False
	while not found:
		temp = random.randrange(0,6)
		if count2 == 0:
			count2 = 6
			temp2 = temp2 + 1
		if bets[temp][1] == temp2:
				if b > 1 and (shifts_b[b-1] != bets[temp][0] and shifts_b[b-2] != bets[temp][0]):
					bets[temp][1] = bets[temp][1] + 1
					count2 = count2 - 1
					print "Day ",b,shifts[b],bets[temp]
					shifts_b.append(bets[temp][0])
					found = True
				if b == 0:
					bets[temp][1] = bets[temp][1] + 1
					count2 = count2 - 1
					print "Day ",b,bets[temp]
					shifts_b.append(bets[temp][0])
					found = True	
				if b == 1 and shifts_b[b-1] != bets[temp][0]:
					bets[temp][1] = bets[temp][1] + 1
					count2 = count2 - 1
					print "Day ",b,bets[temp]
					shifts_b.append(bets[temp][0])
					found = True								

print "DONE!!! with Bet ", shifts_b	


def regular_shift(n):
	if n >0: 
		return n
	n = n -1

print(regular_shift(6))





#	else:
#		count2 = 6;
#		temp2 = temp2 + 1
#		if alephs[temp][1] == temp2:
#			alephs[temp][1] = alephs[temp][1] + 1
#			count2 = count2 -1
#	print "Day ",a, alephs[temp],temp2