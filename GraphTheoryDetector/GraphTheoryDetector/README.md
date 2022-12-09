# Graph Theory Detector

> ref. ALASMARY, Hisham, et al. Analyzing and detecting emerging Internet of Things malware: A graph-based approach. *IEEE Internet of Things Journal*, 2019, 6.5: 8977-8988.

## Introduction

### Description

* The main program is a malware detector.

  * **Input** : a binary file

  * **Output** : its label predicted by ML model
  * **Flow** : 
    * reverse the bin and extract the feature
    * load the model
    * predict


### Feature Extraction

* We reverse the binary file to function call graph(FCG) by r2pipe, then extract the attribute of FCG:

  * number of nodes

  * number of edges

  * density

  * (mean, max, min, median, std) of closeness_centrality


  * (mean, max, min, median, std) of betweenness_centrality


  * (mean, max, min, median, std) of degree_centrality


  * (mean, max, min, median, std) of shortestpaths.avglen 

  The dimension of feature is 23.


## Requirements

* python3
* radare2
* python package
  * r2pipe
  * networkx
  * joblib
  * argparse
  * sklearn


## Usage

* setting path of input file,the feature will be stored in ./feature/

  ```
  python main.py --input-path [FILE_PATH]
  ```

* detect the file

  ```
  cd MD_Model
  python detector.py --model [MODEL]
  ```

  MODEL can be rf, knn, svm, mlp, default: mlp

* e.g.

  ```
  python -W ignore main.py --input-path .\TestingBin\1100a1693fbe43b0ff29c1d5a36011421752e162171683a7053cc1a342cdb11a --model svm 
  python ./MD_Model/detector.py --model svm
  ```

  * ignore the warning message by using '-W ignore'



## Result of Malware Detection

|    Models    | Accuracy | Time cost |
| :----------: | :------: | :-------: |
| RandomForest |   0.97   |   5.01    |
|     KNN      |  0.967   |  165.51   |
|     SVM      |  0.772   |  1606.21  |
|     MLP      |  0.879   |   49.51   |

## Result of Family Classification

|    Models    | Accuracy | Time cost |
| :----------: | :------: | :-------: |
| RandomForest |  0.952   |   4.21    |
|     KNN      |  0.944   |  104.92   |
|     SVM      |   0.71   |  1562.06  |
|     MLP      |  0.887   |   70.99   |
