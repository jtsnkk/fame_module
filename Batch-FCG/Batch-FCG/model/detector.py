import sklearn
import pickle
from param_parser import parameter_parser
import numpy as np
import os

def main(args):
    path=os.path.dirname(os.path.abspath(__file__))
    model_type = "LR"
    model = pickle.load(open(path+'/Model_save/'+model_type+'.pkl','rb'))
    
    feature = np.load(args.target, allow_pickle=True)
    name = feature[-1]
    feature = np.delete(feature,-1)
    test = []
    for i in feature:
        test.append(i)
    
    test = np.array(test)
    label = model.predict(test)

    for i,j in zip(name,label):
        print(i,j)

    

if __name__=='__main__':
    args = parameter_parser()
    main(args)
