import numpy as np
import os
import xgboost
from sklearn import svm
from parser import parameter_parser
from sklearn.feature_extraction.text import CountVectorizer
import r2pipe



def Extraction(filename):
    # OpenFile
    r2 = r2pipe.open(filename)
    # Analyze  
    r2.cmd('aaaa')
    # Extraction
    OpcodeSequence=[]
    DisassembleJ=r2.cmdj('pdj $s')
    if DisassembleJ:
        for instruction in DisassembleJ:
            try:
                if instruction['opcode'].split(' ')[0]:
                    if instruction['opcode'].split(' ')[0] != "invalid":
                        OpcodeSequence.append(instruction['opcode'].split(' ')[0])
            except:
                pass
    return OpcodeSequence

def vectorize(sequence):
    seq = ''
    for i in sequence:
        seq += str(i + ' ')
    X = list()
    X.append(seq)
    vectorizer_count = CountVectorizer(ngram_range = (2, 4))
    x_count = vectorizer_count.fit_transform(X)
    feature_list = vectorizer_count.get_feature_names()
    top_feature= np.load("./top_features_1.npy")
    tmp = []
    for j in range(len(top_feature)):
        if(top_feature[j] in feature_list):
            tmp.append(x_count[:,feature_list.index(top_feature[j])][0,0])
        else:
            tmp.append(0)
    tmp = np.asarray(tmp)
    tmp = tmp.reshape(1,-1)
    return(tmp)
    
    


def main(args):
    # print(args.input_path)
    # print(args.model)
    
    try:
        opcode_sequence = Extraction(args.input_path)
    except:
        print('fail to extract the Opcode.')
        print(0)
        return 0
    
    try:
        feature = vectorize(opcode_sequence)
    except:
        print('fail to extract the feature.')
        print(0)
        return 0
    np.save('./feature/feature',feature)
    


    
if __name__=='__main__':
    args = parameter_parser()
    main(args)
