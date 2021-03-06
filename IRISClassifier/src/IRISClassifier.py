import Algorithmia
import pickle
import numpy as np

client = Algorithmia.client()

#load model into memory
file_path = "data://christophostertag/models/iris_rfc.pkl"
with open(client.file(file_path).getFile().name,"rb") as f:
  model = pickle.load(f)

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
  #try:
  X = [input]
  pred = model.predict(X)
  return X
  #except:
  return "wrong input"
