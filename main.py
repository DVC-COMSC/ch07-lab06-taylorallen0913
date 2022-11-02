
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
numbers2 = []
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 

for i in range(len(numbers1)):
	numbers2.insert(i, numbers1.pop())

print ("The original list: ", numbers1)
# print(numbers2)