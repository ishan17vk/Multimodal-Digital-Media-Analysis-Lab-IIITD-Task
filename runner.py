import time
import os
# import pandas as pd
# import numpy as np
# import tensorflow_text as text
# import tesnsorflow


file_path = ""
fp = open(file_path)
last  = fp.readline()[:18]  # variable to store last timestamp of block
model = keras.models.load_model('./Model_Vader_Keras')

while True:
    fp = open(file_path,"r")
    block = []
    flag = False
    for line in fp:
        if line.startswith(last) == 0:    #ignoring data before last timestamp
            continue
        if line.startswith(last) ==1:    #changing flag when last is encountered
            flag=True
        if flag:
            line = line.replace('\n',"")
            block.append(line)

    print("No of lines in this interval:", len(block)))
    
    time_stamp = list([x[:18] for x in data])
    cleaned_data = list([x[18:].lower() for x in data ])
    prediction = model.predict(cleaned_data)
    prediction = [1 if x > 0.4 else 0 for x in output]

    output = list(zip(time_stamp,output))
    last = block[-1][:19]   # Storing the time of last sentence recorded
    print(f"Predictions for the block starts with timestamp {block[:18]} : ")
    for i in output:
        print(i)
    print("Sleeping ...............")
    time.sleep(300) #making program sleep for 3 mins