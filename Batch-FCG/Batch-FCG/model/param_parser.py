import argparse


def parameter_parser():
    parser = argparse.ArgumentParser(description="Run FCG detector.")

    parser.add_argument('--model',
                        nargs='?',
                        default='LR',
                        help='Select the model(KNN,LR,MLP,RF,SVM).')
    parser.add_argument('--target',
                        nargs='?',
                        default='feature.npy',
                        help='Select the feature file.')
    
    
    return parser.parse_args()
