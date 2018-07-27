#getting input from user for loops and add set
n = int(input())

#declare varibale that will be used
rawList = []
rawSet = set()
finalList = []
finalSet = set()

#loops for getting set from user
for i in range(n):
	getStr = input()
	#replace all punctioation that we don't neeed
	getStr = getStr.replace("{", "")
	getStr = getStr.replace("}", "")
	getStr = getStr.replace(" ", "")
	
	#split the string based on a comma
	getStr = getStr.split(",")
	rawSet = set(getStr)
	rawList.append(rawSet)

#searching for intersection from each set in list
for i in range(len(rawList)-1):
	rawSet = rawSet ^ rawList[i]

#make all the set integer not string
finalSet = set(map(int, rawSet))

#print the set to the screen
print(finalSet)