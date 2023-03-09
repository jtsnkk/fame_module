import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn import ensemble, preprocessing, metrics
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_predict
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import silhouette_score
from scipy.stats import randint as sp_randint
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.manifold import TSNE
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot
import sklearn.metrics as sm
import seaborn as sns
import time
import csv


#### ML model #####

def RF(Feature, Label, n_estimators):
    X_train, X_test, Y_train, Y_test = train_test_split(
        Feature, Label, test_size=0.2)
    print("----------Start RF training--------------")
    start_time = time.time()
    forest = ensemble.RandomForestClassifier(
        n_estimators=n_estimators, n_jobs=-1, random_state=1)
    forest.fit(X_train, Y_train)
    y_predicted = forest.predict(X_test)
    print("RF_accuracy:", accuracy_score(Y_test, y_predicted))
    print("Precision:", precision_score(Y_test, y_predicted, average='macro'))
    print("Recall:", recall_score(Y_test, y_predicted, average='macro'))
    print("F1_score:", f1_score(Y_test, y_predicted, average='macro'))
    print("--- %s seconds ---" % (time.time() - start_time))
    return forest, [accuracy_score(Y_test, y_predicted), precision_score(Y_test, y_predicted, average='macro'), recall_score(Y_test, y_predicted, average='macro'), f1_score(Y_test, y_predicted, average='macro')]


def KNN(Feature, Label, neighbors):
    X_train, X_test, Y_train, Y_test = train_test_split(
        Feature, Label, test_size=0.2)
    print("----------Start KNN training--------------")
    start_time = time.time()
    neigh = KNeighborsClassifier(
        algorithm='auto', n_neighbors=neighbors, n_jobs=-1, p=2)
    neigh.fit(X_train, Y_train)
    y_predicted = neigh.predict(X_test)
    print("KNN_accuracy:", accuracy_score(Y_test, y_predicted))
    print("Precision:", precision_score(Y_test, y_predicted, average='macro'))
    print("Recall:", recall_score(Y_test, y_predicted, average='macro'))
    print("F1_score:", f1_score(Y_test, y_predicted, average='macro'))
    print("--- %s seconds ---" % (time.time() - start_time))
    return neigh, [accuracy_score(Y_test, y_predicted), precision_score(Y_test, y_predicted, average='macro'), recall_score(Y_test, y_predicted, average='macro'), f1_score(Y_test, y_predicted, average='macro')]


def SVM(Feature, Label, C, gamma):
    X_train, X_test, Y_train, Y_test = train_test_split(
        Feature, Label, test_size=0.2)
    print('---start SVM training---')
    start_time = time.time()
    clf = svm.SVC(kernel='rbf', C=C, gamma=gamma)
    clf.fit(X_train, Y_train)
    y_predicted = clf.predict(X_test)
    print("RF_accuracy:", accuracy_score(Y_test, y_predicted))
    print("Precision:", precision_score(Y_test, y_predicted, average='macro'))
    print("Recall:", recall_score(Y_test, y_predicted, average='macro'))
    print("F1_score:", f1_score(Y_test, y_predicted, average='macro'))
    print("--- %s seconds ---" % (time.time() - start_time))
    return clf, [accuracy_score(Y_test, y_predicted), precision_score(Y_test, y_predicted, average='macro'), recall_score(Y_test, y_predicted, average='macro'), f1_score(Y_test, y_predicted, average='macro')]


def MLP(Feature, Label, hidden_layer_sizes, iterations):
    X_train, X_test, Y_train, Y_test = train_test_split(
        Feature, Label, test_size=0.2)
    print('---start MLP training---')
    start_time = time.time()
    mlp = MLPClassifier(hidden_layer_sizes=(hidden_layer_sizes,), max_iter=iterations, alpha=1e-4,
                        solver='sgd', verbose=10, tol=1e-4, random_state=1,
                        learning_rate_init=.1)
    mlp.fit(X_train, Y_train)
    mlp.predict(X_test)
    y_predicted = mlp.predict(X_test)
    print("MLP_accuracy:", accuracy_score(Y_test, y_predicted))
    print("Precision:", precision_score(Y_test, y_predicted, average='macro'))
    print("Recall:", recall_score(Y_test, y_predicted, average='macro'))
    print("F1_score:", f1_score(Y_test, y_predicted, average='macro'))
    print("--- %s seconds ---" % (time.time() - start_time))
    return mlp, [accuracy_score(Y_test, y_predicted), precision_score(Y_test, y_predicted, average='macro'), recall_score(Y_test, y_predicted, average='macro'), f1_score(Y_test, y_predicted, average='macro')]


# def LR(Feature, Label, n_estimators):
#     X_train, X_test, Y_train, Y_test = train_test_split(
#         Feature, Label, test_size=0.2)
#     print("----------Start RF training--------------")
#     start_time = time.time()
#     lr = LogisticRegression(C=C, tol=tol, n_jobs=-1)
#     lr.fit(X_train, Y_train)
#     y_predicted = lr.predict(X_test)
#     print("LR_accuracy:", accuracy_score(Y_test, y_predicted))
#     print("Precision:", precision_score(Y_test, y_predicted, average='macro'))
#     print("Recall:", recall_score(Y_test, y_predicted, average='macro'))
#     print("F1_score:", f1_score(Y_test, y_predicted, average='macro'))
#     print("--- %s seconds ---" % (time.time() - start_time))
#     return lr, [accuracy_score(Y_test, y_predicted), precision_score(Y_test, y_predicted, average='macro'), recall_score(Y_test, y_predicted, average='macro'), f1_score(Y_test, y_predicted, average='macro')]

#### Grid search #######


def RF_grid_search(Feature, Label):
    estimator = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    rf_result = []
    rf_time = []
    for n in estimator:
        print('estimator: ', n)
        start_time = time.time()
        # forest = ensemble.RandomForestClassifier(n_estimators = n, oob_score = True, n_jobs = -1)
        # scores = cross_val_score(forest, Feature,Label, cv=5,scoring='accuracy')
        # rf_result.append(round(scores.mean(dtype=np.float64),4))
        # print("RFcv_accuracy:",round(scores.mean(dtype=np.float64),4))
        rf_result.append(Stratified_CV_RF(Feature, Label, n, 5))
        rf_time.append((time.time() - start_time))
        print("--- %s seconds ---" % (time.time() - start_time))

    plt.plot(estimator, rf_result, 'o-')
    for i in range(len(estimator)):
        plt.text(estimator[i], rf_result[i], rf_result[i])
    plt.xlabel("n_estimator", fontsize=12, labelpad=15)
    plt.ylabel("Accuracy", fontsize=12, labelpad=20)

    return rf_result, rf_time


def KNN_grid_search(Feature, Label):
    k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    knn_result = []
    knn_time = []
    for n in k:
        print('Neigh:', n)
        start_time = time.time()
        # neigh = KNeighborsClassifier(algorithm='auto',n_neighbors=n,n_jobs=-1,p=2)
        # scores = cross_val_score(neigh, Feature,Label, cv=5,scoring='accuracy')
        # knn_result.append(round(scores.mean(dtype=np.float64),4))
        # print("KNNcv_accuracy:",round(scores.mean(dtype=np.float64),4))
        knn_result.append(Stratified_CV_KNN(Feature, Label, n, 5))
        knn_time.append((time.time() - start_time))
        print("--- %s seconds ---" % (time.time() - start_time))

    plt.plot(k, knn_result, 'o-')
    for i in range(len(k)):
        try:
            plt.text(k[i], knn_result[i], knn_result[i])
        except:
            pass
    plt.xlabel("n_neighbor", fontsize=12, labelpad=15)
    plt.ylabel("Accuracy", fontsize=12, labelpad=20)
    return knn_result, knn_time


def SVM_grid_search(Feature, Label):
    par = [0.1, 1, 10, 100, 1000]
    gam = [0.00001, 0.0001, 0.001, 0.01, 0.1]
    svm_result = []
    svm_time = []
    for c in par:
        for g in gam:
            print('C:', c, ' gamma:', g)
            start_time = time.time()
            # clf=svm.SVC(kernel='rbf',C=c,gamma=g)
            # scores = cross_val_score(clf, Feature,Label, cv=5,scoring='accuracy')
            # svm_result.append(round(scores.mean(dtype=np.float64),4))
            # print("SVMcv_accuracy:",round(scores.mean(dtype=np.float64),4))
            svm_result.append(Stratified_CV_SVM(Feature, Label, c, g, 5))
            svm_time.append((time.time() - start_time))
            print("--- %s seconds ---" % (time.time() - start_time))
    sort = []
    tmp = []
    count = 0
    index = 0
    for result in svm_result:
        tmp.append(result)
        count = count+1
        if count == 5:
            sort.append(tmp)
            tmp = []
            count = 0
    sort = np.array(sort)
    print(sort.shape)
    print(sort)

    x_tick = [0.1, 1, 10, 100, 1000]
    y_tick = [0.0001, 0.0001, 0.001, 0.01, 0.1]
    data = {}
    for i in range(5):
        data[x_tick[i]] = sort[i]
    pd_data = pd.DataFrame(data, index=y_tick, columns=x_tick)
    print(pd_data)

    plt.figure(figsize=(5, 5))
    sns.heatmap(pd_data, annot=True, linewidths=5, fmt=".4f")
    plt.xlabel('C', fontsize=10)
    plt.ylabel('gamma', fontsize=10)

    return svm_result, svm_time

###### Cross-validation #######


def RF_cross_validation(Feature, Label, n):
    print('Random Forest Cross validation')
    print('#Estimator: ', n)
    start_time = time.time()
    forest = ensemble.RandomForestClassifier(
        n_estimators=n, oob_score=True, n_jobs=-1)
    scores = cross_validate(forest, Feature, Label, cv=5, scoring=[
                            'accuracy', 'f1_macro', 'precision_macro', 'recall_macro'])
    print("Accuracy:", round(
        scores['test_accuracy'].mean(dtype=np.float64), 4))
    print("Precision:", round(
        scores['test_precision_macro'].mean(dtype=np.float64), 4))
    print("Recall:", round(
        scores['test_recall_macro'].mean(dtype=np.float64), 4))
    print("F1_score:", round(
        scores['test_f1_macro'].mean(dtype=np.float64), 4))
    print("--- %s seconds ---" % (time.time() - start_time))
    return round(scores['test_accuracy'].mean(dtype=np.float64), 4)


def LR_cross_validation(Feature, Label, C, tol):
    print('Logistic Regression Cross validation')
    print('C:', C, 'tol:', tol)
    start_time = time.time()
    LR = LogisticRegression(C=C, tol=tol, n_jobs=-1)
    scores = cross_validate(LR, Feature, Label, cv=5, scoring=[
                            'accuracy', 'f1_macro', 'precision_macro', 'recall_macro'])
    print("Accuracy:", round(
        scores['test_accuracy'].mean(dtype=np.float64), 4))
    print("Precision:", round(
        scores['test_precision_macro'].mean(dtype=np.float64), 4))
    print("Recall:", round(
        scores['test_recall_macro'].mean(dtype=np.float64), 4))
    print("F1_score:", round(
        scores['test_f1_macro'].mean(dtype=np.float64), 4))
    print("--- %s seconds ---" % (time.time() - start_time))
    return round(scores['test_accuracy'].mean(dtype=np.float64), 4)


def KNN_cross_validation(Feature, Label, n):
    print('K-near neighbors Cross validation')
    print('#Neighs: ', n)
    start_time = time.time()
    neigh = KNeighborsClassifier(
        algorithm='auto', n_neighbors=n, n_jobs=-1, p=2)
    scores = cross_validate(neigh, Feature, Label, cv=5, scoring=[
                            'accuracy', 'f1_macro', 'precision_macro', 'recall_macro'])
    print("Accuracy:", round(
        scores['test_accuracy'].mean(dtype=np.float64), 4))
    print("Precision:", round(
        scores['test_precision_macro'].mean(dtype=np.float64), 4))
    print("Recall:", round(
        scores['test_recall_macro'].mean(dtype=np.float64), 4))
    print("F1_score:", round(
        scores['test_f1_macro'].mean(dtype=np.float64), 4))
    print("--- %s seconds ---" % (time.time() - start_time))
    return round(scores['test_accuracy'].mean(dtype=np.float64), 4)


def MLP_cross_validation(Feature, Label, size, iterations):
    print('Multilayer Perceptron Cross validation')
    print('Hidden Layer Size:', size, ' Iterations:', iterations)
    start_time = time.time()
    mlp = MLPClassifier(hidden_layer_sizes=(size,), max_iter=iterations, alpha=1e-4,
                        solver='sgd', verbose=10, tol=1e-4, random_state=1,
                        learning_rate_init=.1)
    scores = cross_validate(mlp, Feature, Label, cv=5, scoring=[
                            'accuracy', 'f1_macro', 'precision_macro', 'recall_macro'])
    print("Accuracy:", round(
        scores['test_accuracy'].mean(dtype=np.float64), 4))
    print("Precision:", round(
        scores['test_precision_macro'].mean(dtype=np.float64), 4))
    print("Recall:", round(
        scores['test_recall_macro'].mean(dtype=np.float64), 4))
    print("F1_score:", round(
        scores['test_f1_macro'].mean(dtype=np.float64), 4))
    print("--- %s seconds ---" % (time.time() - start_time))
    return round(scores['test_accuracy'].mean(dtype=np.float64), 4)


def SVM_cross_validation(Feature, Label, C, gamma):
    print('Support Vector Machine Cross Validation')
    print('C:', C, ' Gamma:', gamma)
    start_time = time.time()
    clf = svm.SVC(kernel='rbf', C=C, gamma=gamma)
    scores = cross_validate(clf, Feature, Label, cv=5, scoring=[
                            'accuracy', 'f1_macro', 'precision_macro', 'recall_macro'])
    print("Accuracy:", round(
        scores['test_accuracy'].mean(dtype=np.float64), 4))
    print("Precision:", round(
        scores['test_precision_macro'].mean(dtype=np.float64), 4))
    print("Recall:", round(
        scores['test_recall_macro'].mean(dtype=np.float64), 4))
    print("F1_score:", round(
        scores['test_f1_macro'].mean(dtype=np.float64), 4))
    print("--- %s seconds ---" % (time.time() - start_time))
    return round(scores['test_accuracy'].mean(dtype=np.float64), 4)


####  Stratified_CV  #######
'''
This cross-validation object is a variation of KFold that returns stratified folds.
The folds are made by preserving the percentage of samples for each class.
'''
def Stratified_CV_RF(Feature, Label, n_estimators, cv):
    Result = []
    skf = StratifiedKFold(n_splits=cv)
    round_c = 1
    for train_index, test_index in skf.split(Feature, Label):
        Train_Feature, Train_Label = Feature[train_index], Feature[test_index]
        Test_Feature, Test_Label = Label[train_index], Label[test_index]
        print('Round:', round_c)
        forest = ensemble.RandomForestClassifier(
            n_estimators=n_estimators, n_jobs=-1)

        forest.fit(Train_Feature, Train_Label)
        y_predicted = forest.predict(Test_Feature)
        
        Result.append([accuracy_score(Test_Label, y_predicted), precision_score(Test_Label, y_predicted, average='macro'), recall_score(
            Test_Label, y_predicted, average='macro'), f1_score(Test_Label, y_predicted, average='macro')])
        round_c += 1

    Result = np.array(Result)
    with open('RF.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([round(np.mean(Result[0]), 4), round(np.mean(
            Result[1]), 4), round(np.mean(Result[2]), 4), round(np.mean(Result[3]), 4)])
    return round(np.mean(Result[0]), 4)


def Stratified_CV_KNN(Feature, Label, neighbors, cv):
    Result = []
    skf = StratifiedKFold(n_splits=cv)
    round_c = 1
    for train_index, test_index in skf.split(Feature, Label):
        Train_Feature = []
        Train_Label = []
        Test_Feature = []
        Test_Label = []
        print('Round:', round_c)
        for index in train_index:
            Train_Feature.append(Feature[index])
            Train_Label.append(Label[index])
        for index in test_index:
            Test_Feature.append(Feature[index])
            Test_Label.append(Label[index])
        neigh = KNeighborsClassifier(
            algorithm='auto', n_neighbors=neighbors, n_jobs=-1, p=2)
        neigh.fit(Train_Feature, Train_Label)
        y_predicted = neigh.predict(Test_Feature)
        Result.append([accuracy_score(Test_Label, y_predicted), precision_score(Test_Label, y_predicted, average='macro'), recall_score(
            Test_Label, y_predicted, average='macro'), f1_score(Test_Label, y_predicted, average='macro')])
        round_c += 1

    Result = np.array(Result)
    with open('KNN.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([round(np.mean(Result[0]), 4), round(np.mean(
            Result[1]), 4), round(np.mean(Result[2]), 4), round(np.mean(Result[3]), 4)])
    return round(np.mean(Result[0]), 4)


def Stratified_CV_SVM(Feature, Label, C, Gamma, cv):
    Result = []
    skf = StratifiedKFold(n_splits=cv)
    round_c = 1
    for train_index, test_index in skf.split(Feature, Label):
        Train_Feature = []
        Train_Label = []
        Test_Feature = []
        Test_Label = []
        print('Round:', round_c)
        for index in train_index:
            Train_Feature.append(Feature[index])
            Train_Label.append(Label[index])
        for index in test_index:
            Test_Feature.append(Feature[index])
            Test_Label.append(Label[index])
        clf = svm.SVC(kernel='rbf', C=C, gamma=Gamma)
        clf.fit(Train_Feature, Train_Label)
        y_predicted = clf.predict(Test_Feature)
        Result.append([accuracy_score(Test_Label, y_predicted), precision_score(Test_Label, y_predicted, average='macro'), recall_score(
            Test_Label, y_predicted, average='macro'), f1_score(Test_Label, y_predicted, average='macro')])
        round_c += 1

    Result = np.array(Result)
    with open('SVM.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([round(np.mean(Result[0]), 4), round(np.mean(
            Result[1]), 4), round(np.mean(Result[2]), 4), round(np.mean(Result[3]), 4)])

    return round(np.mean(Result[0]), 4)
