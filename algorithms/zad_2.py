from random import randint # or it is possible to use random (0-1.0)
randList = []
def bubbleSort(list):
	n = len(list)

	while n > 1:
		swap = False
		for i in range(0,n-1):
			if list[i] > list[i+1]:
				list[i], list[i+1] = list[i+1], list[i]
				swap = True
		n -= 1
		if swap == False:
			break;
	return list

for x in range(0,50):
    randList.append(randint(-999,999))
print(randList)
bubbleSort(randList)
print(randList)
