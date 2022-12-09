from . import graphity
import numpy as np
import networkx as nx
import r2pipe
from joblib import load
#from param_parser import parameter_parser
from . import param_parser

def bin2fcg(path):
    '''
    param: binary file path
    return: a string describe the FCG in .dot form
    '''

    # OpenFile
    r2 = r2pipe.open(path)
    # Analyze  
    r2.cmd('aaaa')
    # Extract and return the dot string 
    command = 'agCd'
    G = r2.cmd(command)
    return G

def Extract_feature(dotString):
    '''
    param: a string describe the FCG in .dot form
    return: feature vector of the sample
    '''

    feature=[]
    #Create graph
    G=graphity.create_graph(dotString)

    # append #nodes & # edges
    feature.append(G.number_of_nodes())
    feature.append(G.number_of_edges())

    # append Density
    feature.append(graphity.get_density(G))

    # append Closeness Centrality
    for i in graphity.closeness_centrality(G):
        feature.append(i)

    # append Betweeness Centrality
    for i in graphity.betweeness_centrality(G):
        feature.append(i)

    # append Degree Centrality
    for i in graphity.degree_centrality(G):
        feature.append(i)

    # append Shortest Path
    for i in graphity.shortest_path(G):
        feature.append(i)

    return feature

def Scaling(feature):
    '''
    param: feature vector
    return: feature vector after scaling
    '''
    scaler = load('scaler.joblib')
    feature = scaler.transform(feature)
    return feature


def main(args):
    # print(args.input_path)
    # print(args.model)
    try:
        dotString = bin2fcg(args.input_path)
    except:
        print('fail to extract the FCG.')
        print(0)
        return 0
    
    try:
        feature = Extract_feature(dotString)
    except:
        print('fail to extract the feature.')
        print(0)
        return 0

    feature = np.array(feature).reshape(1,-1)
    feature = Scaling(feature)  
    np.save('./feature/feature',feature)

    

if __name__=='__main__':
    args = parameter_parser()
    main(args)
