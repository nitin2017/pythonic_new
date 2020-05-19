# list vs generator 
# memory usage , time 
# when to use list , when to use generator 
import time 
t0 = time.time()
#l = [i**2 for i in range (100000000)] # 10 million # 50.12322449684143 seconds 
g = (i**2 for i in range (10000000))
t1 = time.time()
print(t1-t0)



