def sample_selection_sort(list_1):
    '''


    '''
    length = len(list_1)
    for i in range(length):
        min = i
        for j in range(i,length):
            if list_1[j] < list_1[min]:
                min = j
        if min != i:
            list_1[i], list_1[min] = list_1[min], list_1[i]
    return list_1
def test():
    list_1 = [3,4,1,6,2,7,5]
    assert sample_selection_sort(list_1) == [1,2,3,4,5,6,7]

    return 'test pass'

print(test())