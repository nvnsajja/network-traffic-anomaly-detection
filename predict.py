import numpy as np
import pandas as pd
from keras.models import Model, load_model
import subprocess
import time

data = pd.read_csv("files/Data.csv")
data = data.drop(['Unnamed: 0'],axis=1)
model = load_model("DanminiDoorbell_Model.h5")
predictions = model.predict(data)
#print("predictions :",predictions)
mse = np.nanmean(np.power(data - predictions, 2), axis=1)

threshold = np.nanmean(mse)+np.nanstd(mse)
#print("mse :",mse)

pred = [1 if e > threshold else 0 for e in mse]
print(pred)

Bengin_count = 0
for ele in pred:
	if (ele == 0):
		Bengin_count = Bengin_count + 1

Malicious_count = 0
for ele in pred:
	if (ele == 1):
		Malicious_count = Malicious_count + 1


print("Bengin : ",Bengin_count)
print("Malicious : ",Malicious_count)
pred.append(0)

for element in pred:
	df = pd.DataFrame(data={'Pred': [element]})
	df.to_csv("files/Visualization.csv")
	time.sleep(.200)
exit()
