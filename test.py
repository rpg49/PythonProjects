#Code to test for loop with if condition together
l1 = ['ghj','diff']
f = 'Cancelnew'
if [x for x in l1 if x not in f]:
    print([x for x in l1 if x not in f])
    print('No list element is in f')
    print('loop ended')
