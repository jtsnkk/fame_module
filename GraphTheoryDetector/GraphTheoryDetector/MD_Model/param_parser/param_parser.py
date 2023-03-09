import argparse


def parameter_parser():
    parser = argparse.ArgumentParser(description="Run GraphTheoryDetector.")

    parser.add_argument('--input-path',
                        nargs='?',
                        default='./TestingBin/0000dc2f3c8bde2d3b61cd1ba3aa5e839c0a7bf432d2e06a88a7ce3b199453e7',
                        help='input binary file.')

    parser.add_argument('--model',
                        nargs='?',
                        default='mlp',
                        help='Select the model(rf, knn, svm, mlp).')
    
    parser.add_argument('--target',
                        nargs='?',
                        default='feature.npy',
                        help='Select the feature file.')
    
    return parser.parse_args()
