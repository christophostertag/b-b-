import Algorithmia
import pickle
import numpy as np

client = Algorithmia.client()

#load model into memory
file_path = "data://christophostertag/models/iris_rfc.pkl"
model = pickle.load(open(client.file(file_path).getFile().name,"rb"))

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
  #try:
  X = np.array(input).reshape(-1,4)
  pred = model.predict(X)
  return pred
  #except:
  return "wrong input"