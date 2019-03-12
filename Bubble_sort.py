
def swap(list_1, i, j):
	'''
	exchange i-th and j-th element in a list
	'''
	temp = list_1[i]
	list_1[i] = list_1[j]
	list_1[j] = temp
	return list_1
def bubble_sort_simple(list_1):
	'''
	Simply compare every element with the rest
	'''
	length = len(list_1)
	for i in range(length):
		for j in range (i,length):
			if list_1[i] <= list_1[j]:
				continue
			else:
				swap(list_1,i,j)

	return list_1
def bubble_sort_basic(list_1):

	length = len(list_1)
	for i in range(length):
		for j in reversed(range(i,length)):
			if list_1[j-1]<=list_1[j]:
				continue
			else:
				swap(list_1,j-1,j)
	return list_1
def bubble_sort_opt(list_1):
	length = len(list_1)

	for i in range(length):
		print(i,'apple')
		exitFlag = True
		for j in reversed(range(i+1,length)):
			if list_1[j-1]<=list_1[j]:
				continue
			else:
				swap(list_1,j-1,j)
				print(list_1,'organge',j)
				exitFlag = False
		if exitFlag :
			print('banana')
			return list_1
	return list_1

def test():
	list_1 = [3,4,1,6,2,7,5]
	list_2 = [2,1,3,4,5,6,7]
	assert bubble_sort_simple(list_1) == [1,2,3,4,5,6,7]
	assert bubble_sort_basic(list_1) == [1,2,3,4,5,6,7]
	assert bubble_sort_opt(list_2) == [1,2,3,4,5,6,7]
	return 'test pass'

print(test())
