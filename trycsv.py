import csv
import time


csvfile = open("test.csv", "w")

cw = csv.writer(csvfile)
start_time = time.time()
for i in range(10000):
    cw.writerow([1,2,3,4,5,6,7,8,9])
print("--- Executed in %s seconds ---" %(time.time() - start_time))
csvfile.close()