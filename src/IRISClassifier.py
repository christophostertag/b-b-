import Algorithmia
import pickle
#import numpy as np

client = Algorithmia.client()

#load model into memory
def load_model(file_path):
    # Get file by name
    # Open file and load model
    model_path = client.file(file_path).getFile().name
    # Open file and load model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
        return model

file_path = "data://christophostertag/models/iris_rfc.pkl"
model = load_model(file_path)

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
  #try:
  X = [input]
  pred = model.predict(X)
  return pred
  #except:
  return "wrong input"
  
print(apply([1,2,3,4]))