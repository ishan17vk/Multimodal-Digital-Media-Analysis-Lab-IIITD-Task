import os
import time

dataCol = "/usr/bin/python3 /host-fs/var/log/harsh/dataCollection.py"
pred = "/usr/bin/python3 /host-fs/var/log/harsh/prediction.py"

print("IN WRAPPER JUST BEFORE DATA COLLECTION")
print(os.system(dataCol))
print("IN WRAPPER JUST BECAUSE PREDICTION")
print(os.system(pred))
print("Going to Master...")