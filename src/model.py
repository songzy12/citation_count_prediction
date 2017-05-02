import code
import pickle
import numpy as np
from sklearn import datasets, linear_model

from feature import get_features
from util import get_train

MODEL_DIR = "/home/songzy/HW3/model/"

def get_training_set():
    """
    return: a list of features and their correspond targets
    """
    id2count = get_train()
    data = []
    target = []
    for id_, count in id2count.items():
        data.append(get_features(id_))
        target.append(count)
    return np.asarray(data), np.asarray(target)

def train():
    citation_X, target = get_training_set()
   
    # TODO
    citation_X_train = citation_X[:1000]
    citation_X_test = citation_X[-1000:]
    citation_y_train = target[:1000]
    citation_y_test = target[-1000:]

    regr = linear_model.LinearRegression()
    #code.interact(local=locals())
    regr.fit(citation_X_train, citation_y_train)
    print('Coefficients: \n', regr.coef_)
    print("Mean squared error: %.2f"
          % np.mean((regr.predict(citation_X_test) - citation_y_test) ** 2)**0.5)
    print('Variance score: %.2f' % regr.score(citation_X_test, citation_y_test))
    return regr 

def dump_model(model,path=MODEL_DIR+'regr.pkl'):
    with open(path, 'w') as f:
        pickle.dump(model, f)
        
def load_model(path=MODEL_DIR+'regr.pkl'):
    """
    return: the model
    """
    with open(path) as f:
        model = pickle.load(f) 
    return model

if __name__ == '__main__':
    model = train()
    dump_model(model)
