import Algorithmia
import pickle

client = Algorithmia.client()

file_path = "data://christophostertag/models/iris_rfc.pkl"

client.file(file_path).getFile().name

  model = pickle.load(open(client.file(file_path).getFile().name,"rb"))

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
  pred = model.predict(input)
  return pred