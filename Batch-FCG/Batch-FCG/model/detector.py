import sklearn
import pickle
from param_parser.param_parser import parameter_parser
import numpy as np
import os

def main(args):
    path=os.path.dirname(os.path.abspath(__file__))
    model_type = "SVM"
    model = pickle.load(open(path+'/Model_save/'+model_type+'.pkl','rb'))
    
    feature = np.load(args.model)
    label = model.predict(feature)
    print(label)
    

if __name__=='__main__':
    args = parameter_parser()
    main(args)
