import Algorithmia
import pickle

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
  model = pickle.load(open("data://christophostertag/models/iris_rfc.pkl","rb"))
  pred = model.predict(input)
  return pred