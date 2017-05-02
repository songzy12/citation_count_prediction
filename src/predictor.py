from util import get_test, dump_results
from feature import get_features
from model import load_model 

def get_results(author_test):
    """
    param: a list of author ids
    return: a list of tuple (author id, predicted citation count)
    """
    results = []
    model = load_model()
    # TODO
    test_features = [get_features(id_) for id_ in author_test]
    return zip(author_test, max(0, model.predict(test_features)))
 
if __name__ == '__main__':
    author_test = get_test()
    results = get_results(author_test)
    dump_results(results)
