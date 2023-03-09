import numpy as np
import pandas as pd
import pickle
from param_parser.param_parser import parameter_parser
import os


def main():

    path=os.path.dirname(os.path.abspath(__file__))
    
    label_dict = {0:'BenignWare', 1:'Malware'}
    feature = np.load(args.target)
    model_path = path+"/model_save/detection_model"
    model = pd.read_pickle(model_path)
    result = model.predict([feature])
    result = np.argmax(result)
    print("result :",label_dict[result])

if __name__=='__main__':
    args = parameter_parser()
    main()


