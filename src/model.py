import code
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

from feature import get_features
from util import get_train, logger

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

    regr = RandomForestRegressor(n_estimators=100, n_jobs=2)
    #regr = linear_model.LinearRegression()
    #regr = SVR(C=1.0, epsilon=0.2)

    #scores = cross_val_score(regr, citation_X, target, cv=10, scoring='neg_mean_squared_error')
    #logger.info('Mean squared error: %0.2f (+/- %0.2f)' % (scores.mean(), scores.std() * 2))

    citation_X_train = citation_X[:-1000]
    citation_X_test = citation_X[-1000:]
    citation_y_train = target[:-1000]
    citation_y_test = target[-1000:]

    #regr.fit(citation_X_train, citation_y_train)
    regr.fit(citation_X, target)
    logger.info('Variance score: %.2f' % regr.score(citation_X, target))
    logger.info("Mean squared error: %.2f"
                % np.mean((regr.predict(citation_X_test) - citation_y_test) ** 2)**0.5)
    return regr


def dump_model(model, path=MODEL_DIR+'regr.pkl'):
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
    logger.info("model training begins")
    model = train()
    logger.info("model training finished")
    dump_model(model)
