import pandas as pd
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix

""" Discretization SCRIPT ============================================================="""
def main_preprocess(dataset_path, datactrl):
    col_count = 37            

    dataset = pd.read_csv(dataset_path)
    np.set_printoptions(formatter={'float_kind':'{:0f}'.format})

    if datactrl != 1:
        indexNames = dataset[ dataset['DECISION_DENSITY'] == '?' ].index 
        dataset.drop(indexNames , inplace=True)

    j = 0
    for i in range(col_count):
        if dataset.iloc[:, i-j].nunique()==1:
            dropName = dataset.iloc[:, i-j].name
            dataset = dataset.drop(dropName, axis=1)
            j = j + 1
    col_count = col_count - j

    array = dataset.values
    feature_data = array[:,0:col_count]
    target_data = array[:,col_count]
    return dataset, feature_data, target_data

""" Discretization SCRIPT """
def main_discretize(feature_data):
    from sklearn.preprocessing import KBinsDiscretizer

    est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='kmeans')
    est.fit(feature_data)
    discretize_data = est.transform(feature_data)
    discretize_data = discretize_data.astype(int)
    return discretize_data

""" Feature Extraction SCRIPT """
def feature_extract(discretize_data, target_data, num_fea):
    import scipy.io
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import cross_validate
    from sklearn.model_selection import train_test_split
    from sklearn import svm
    from skfeature.function.information_theoretical_based import MRMR

    feature_extraction = MRMR.mrmr(discretize_data, target_data, n_selected_features=num_fea)
    return feature_extraction

def concat(selected_data, target_data):
    import numpy as np
    concat_data = np.arange(8349).reshape(759,11)
    concat_data = np.concatenate((selected_data, target_data[:,None]), axis=1)
    return concat_data

""" HELPER FUNCTION: GENERIC CLASSIFIER """
def generic_clf(Y_train, X_train, Y_test, X_test, clf):
    clf.fit(X_train,Y_train)
    pred_train = clf.predict(X_train)
    pred_test = clf.predict(X_test)
    return pred_train, pred_test

""" HELPER FUNCTION: GET ERROR RATE """
def get_error_rate(pred, Y):
    return sum(pred != Y) / float(len(Y))
