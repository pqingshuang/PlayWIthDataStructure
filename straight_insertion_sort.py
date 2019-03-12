def straight_insertion_sort(list_1):
    length = len(list_1)
    for i in range(1,length):
        temp = list_1[i]
        j = i-1
        while temp < list_1[j] and j>=0:
            list_1[j+1] = list_1[j]
            j -=1
        list_1[j+1] = temp

    return list_1
def test():
    list_1 = [3,4,1,6,2,7,5]
    assert straight_insertion_sort(list_1) == [1,2,3,4,5,6,7]
    return 'test pass'

print(test())