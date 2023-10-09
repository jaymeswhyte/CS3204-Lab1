from random import *
import time

def insertionsort(mylist):
    n = len(mylist)
    i = 1
    while i < n:
        j = i-1
        while mylist[i] < mylist[j] and j > -1:
            j -= 1
        temp = mylist[i]
        k = i-1
        while k > j:
            mylist[k+1] = mylist[k]
            k -= 1
        mylist[k+1] = temp
        i += 1

for n in range(1, 151):
    list = []
    for i in range((n*100)+1):
        list.append(randint(1, 100000))
    start_time = time.perf_counter()
    insertionsort(list)
    end_time = time.perf_counter()
    timetaken = end_time-start_time
    if(n%25==0):
        print(f"Time taken to insertion sort list of length {n*100}: {timetaken}")