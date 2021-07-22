##leetcode problem solution

#cout prime numbers

def getCountPrimeCount(n):    
    if n <= 2:
        return 0
    count = 0
    primelist = [False for i in range(n+1)]
    for i in range(2, n):
        #print(i)
        if primelist[i] == False:
            count += 1
            j = 2
            while i*j < n:
                primelist[i*j] = True
                j += 1
    return count

