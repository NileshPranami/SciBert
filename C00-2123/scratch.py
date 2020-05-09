import pandas as pd
import numpy as np
from bert_serving.client import BertClient
import json

FILE = "file2.csv"

df = pd.read_csv(FILE)

Idx = []
embd = []

client = BertClient(check_length=False)
for i, line in enumerate(df["Reference Text"]):
	Idx.append(i)
	embd.append(client.encode([line]))


with open("file2_id.json", "w") as f:
	json.dump(Idx, f)

np.save("file2_embd.npy", embd)