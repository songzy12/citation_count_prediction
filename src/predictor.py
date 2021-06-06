import numpy as np

from util import get_test, dump_results, logger
from feature import get_features, name2author
from model import load_model


def get_results(author_test):
    """
    param: a list of author ids
    return: a list of tuple (author id, predicted citation count)
    """
    results = []
    model = load_model()
    test_features = [get_features(id_) for id_ in author_test]
    ids = map(lambda x: name2author[x].id, author_test)
    prediction = model.predict(test_features)
    return zip(ids, np.maximum(0, prediction))


if __name__ == '__main__':
    author_test = get_test()
    logger.info('%d test data loaded' % len(author_test))
    results = get_results(author_test)
    logger.info('%d prediction results dumped' % len(results))
    dump_results(results)
