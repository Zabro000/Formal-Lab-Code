import csv
import time
Data = [ 5.5, 3.31231213,  7990 ]
with open('writing_test.csv' , 'w') as f:
    write = csv.writer(f)
    write.writerow(Data)


while(True):
    with open('writing_test.csv' , 'a') as f:
        write = csv.writer(f)
        write.writerow(Data)
    time.sleep(5)
