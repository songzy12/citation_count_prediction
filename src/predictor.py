from util import get_test, dump_results
from feature import get_features
from model import load_model, get_citation_count

def get_results(author_test):
    """
    param: a list of author ids
    return: a list of tuple (author id, predicted citation count)
    """
    results = []
    model = load_model()
    for id_ in author_test:
        results += (id_, predict(id_, model)),
    return results
 
def predict(id_, model):
    """
    param: a single author id
    return: the predicted citation count
    """
    features = get_features(id_)
    return get_citation_count(model, features)
        
if __name__ == '__main__':
    author_test = get_test()
    results = get_results(author_test)
    dump_results(results)
