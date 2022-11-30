def multilistas(list1,list2):
    
    list3 = []
    
    for x in range(0, 10):
        
        list3.append(list1[x] * list2[x])
        
    print('Terceira lista:', list3)

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Primeira lista:", listA)
print("Segunda lista:", listB)

multilistas(listA, listB)