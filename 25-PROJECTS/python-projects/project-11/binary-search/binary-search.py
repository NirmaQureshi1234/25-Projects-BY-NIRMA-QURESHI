import random
import time

def native_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target , low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
        
    if high < low:
        return -1
    
    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        return midpoint
    elif  target < l[midpoint]:
        return binary_search(l, target , low, midpoint - 1)
    else:
        return binary_search(l, target , midpoint + 1, high)
    
if __name__ == '__main__':
    # l =[1,3,5,10,12]
    # target = 10
    # print(native_search(l, target))
    # print(binary_search(l, target))
    
    lenght = 10000
    sorted_list = set()
    while len(sorted_list) < lenght:
        sorted_list.add(random.randint(-3*lenght, 3*lenght))
    sorted_list = sorted(list(sorted_list))
    start=time.time()
    for target in sorted_list:
        native_search(sorted_list, target)
    end=time.time()
    print("Native Search Time: ", (end-start)/lenght ,"seconds")
    
    start=time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end=time.time()
    print("Binary Search Time: ", (end-start)/lenght ,"seconds")