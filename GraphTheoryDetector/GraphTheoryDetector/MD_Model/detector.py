import numpy as np
import os
from param_parser.param_parser import parameter_parser
from joblib import load

def Predict(X,clf):
    '''
    param: X (feature vector)
    return: y (label), 0 for benign, 1 for malware
    '''
    path=os.path.dirname(os.path.abspath(__file__))
    
    model = load(path+'/model_save/'+clf+'.joblib')

    label = model.predict(X)
    return label


def main(args):
    
    feature = np.load(args.target)
    result = Predict(feature,"mlp" )
    print(result)



if __name__=='__main__':
    args = parameter_parser()
    main(args)
