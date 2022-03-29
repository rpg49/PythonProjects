#Code to test for loop with if condition together

l1 = ['ghj','diff']
f = 'Cancelnew'
if [x for x in l1 if x not in f]:
    print([x for x in l1 if x not in f])
    print('No list element is in f')
    print('loop ended')


#count bits leetcode problem

def countBits(n):
    list1 = []
    list1.append(0)
    for i in range(1, n):
        list1[i] = list1[i/2] + i%2
    return list1
count = countBits(5)
print('Count = ',count)       

#leetcode problem

##Demo 
print("git pull")



