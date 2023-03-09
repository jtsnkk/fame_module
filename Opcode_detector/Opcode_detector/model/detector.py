import numpy as np
import os
from parser.parser import parameter_parser
import joblib as jb
    
def Predict(X,clf):
    '''
    param: X (feature vector)
    return: y (label), 1 for benign, 0 for malware
    '''
    path=os.path.dirname(os.path.abspath(__file__))

    model = jb.load(path+'/model_save/' + clf)
    label = model.predict(X)
    return label


def main(args):  
    table = {0:'Malware',1:'Benignware'}
    feature = np.load(args.target)
    result = Predict(feature,"SVM")
    result = int(result[0])
    print(table[result])
    return table[result]    
    

if __name__=='__main__':
    args = parameter_parser()
    main(args)
