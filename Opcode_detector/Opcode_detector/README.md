# Opcode N-gram

---
>ref. Li, Xiang, et al. "An adversarial machine learning method based on OpCode N-grams feature in malware detection." 2020 IEEE Fifth International Conference on Data Science in Cyberspace (DSC). IEEE, 2020.

---
## Introduction

### Descripition

* This is a malware detector which use the opcode as feature
    
    - Input:a binary file
    
    - output:the label predicted by Machine Learning model
    
### Feature Extraction

* feature 
    - opcode sequence

* extracted tool
    
     - radare2 4.3.1

## Requirement
---
* python3
* radare2
* python package
    - r2pipe
    - sklearn
    - joblib
    - xgboost

## File
* FC_model : the models are responsible for classify the malware family (saved by joblib)
* MD_model : the models are responsible for classify the malware or benignware (saved by joblib)
* TestingBin : the file that can test this detector
* main.py : the detector
* parser.py : for parsing args
* top_feature_1.npy : save the training data about vectorize the opcode sequence

## Usage
* setting path of input file
> python main.py --input-path [FILE_PATH]

* select the model
> python detector.py --model [MODEL]

MODEL can be xgboost, SVM  default: xgboost



* e.g.
```
 python main.py --input-path ./TestingBin/malware/00a2bd396600e892da75c686be60d5d13e5a34824afd76c02e8cf7257d2cf5c5
 
 cd model/

 python detector.py --model svm
```

### Accuracy
* Detect
    * SVM : 0.963
    * xgboost : 0.9963


